import hashlib
import jwt


SECRET_KEY = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'

class Token:

    def generateToken(self, username, input_password, query_result):
        if not query_result:
            raise ValueError('User not found')

        salt, password, role = query_result[0]
        hashed_password = hashlib.sha512((input_password + salt).encode()).hexdigest()

        if password.lower() != hashed_password.lower():
            raise ValueError('Incorrect Password')

        payload = {"role": role}
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

class Restricted:
    def access_Data(self, authorization_header):
        if authorization_header is None:
            return False
        try:
            token = authorization_header.replace('Bearer ', '')
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            return False

        #return 'role' in decoded_token
        if 'role' in decoded_token:
            return 'You are under protected data'
        else:
            return False
