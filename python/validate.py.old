import ipaddress

class IpValidate:
    def validate_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

