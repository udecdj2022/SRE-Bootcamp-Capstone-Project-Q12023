from flask import Flask, jsonify, request, abort
import mysql.connector

from convert import CidrMaskConvert
from methods import Token, Restricted
from validate import IpValidate


app = Flask(__name__)
login = Token()
protected = Restricted()
converter = CidrMaskConvert()
validator = IpValidate()

@app.route("/")
def url_root():
    return "OK"

# Health check
@app.route("/_health")
def url_health():
    return "OK"

# Login endpoint
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Connect to the database
    try:
        conn = mysql.connector.connect(
            host='sre-bootcamp.czdpg2eovfhn.us-west-1.rds.amazonaws.com',
            user='secret',
            password='jOdznoyH6swQB9sTGdLUeeSrtejWkcw',
            database='bootcamp_tht'
        )

        cursor = conn.cursor()
        cursor.execute(f"SELECT salt, password, role from users where username ='{username}';")
        result = cursor.fetchall()
        
        token = login.generateToken(username, password, result)
        if token is not False:
            return jsonify({"data": token})

        abort(401)

    except mysql.connector.Error as e:
        abort(500, str(e))

    finally:
        cursor.close()
        conn.close()



@app.route("/cidr-to-mask")
def url_cidr_to_mask():
    auth_header = request.headers.get('Authorization')
    if not protected.access_Data(auth_header):
        abort(401)

    cidr = request.args.get('value')
    mask = converter.cidr_to_mask(cidr)

    if mask is not None:
        return jsonify({
            "function": "cidrToMask",
            "input": cidr,
            "output": mask
        })

    abort(400, "Invalid CIDR notation")


@app.route("/mask-to-cidr")
def url_mask_to_cidr():
    auth_header = request.headers.get('Authorization')
    if not protected.access_Data(auth_header):
        abort(401)

    mask = request.args.get('value')
    cidr = converter.mask_to_cidr(mask)

    if cidr is not None:
        return jsonify({
            "function": "maskToCidr",
            "input": mask,
            "output": cidr
        })

    abort(400, "Invalid subnet mask")



@app.route("/validate-ip")
def url_validate_ip():
    auth_header = request.headers.get('Authorization')
    if not protected.access_Data(auth_header):
        abort(401)

    ip = request.args.get('value')
    result = validator.validate_ip(ip)

    return jsonify({
        "function": "validateIp",
        "input": ip,
        "output": result
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

