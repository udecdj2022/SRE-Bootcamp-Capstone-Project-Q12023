import ipaddress

class CidrMaskConvert:
    def cidr_to_mask(self, cidr):
        try:
            cidr = int(cidr)
            if cidr < 0 or cidr > 32:
                return None
            mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
            octets = [str((mask >> i) & 0xff) for i in (24, 16, 8, 0)]
            return '.'.join(octets)
        except ValueError:
            return None

    def mask_to_cidr(self, mask):
        try:
            octets = [int(octet) for octet in mask.split('.')]
            if len(octets) != 4:
                return None
            if not all(0 <= octet <= 255 for octet in octets):
                return None
            binary_str = ''.join([bin(octet)[2:].zfill(8) for octet in octets])
            cidr = len(binary_str.rstrip('0'))
            return str(cidr)
        except ValueError:
            return None


class IpValidate:
    def validate_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

