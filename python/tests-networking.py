from convert import *
import unittest
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.convert = CidrMaskConvert()
        self.validate = IpValidate()

    def test_valid_cidr_to_mask(self):
        self.assertEqual('128.0.0.0', self.convert.cidr_to_mask('1'))

    def test_valid_mask_to_cidr(self):
        self.assertEqual('1', self.convert.mask_to_cidr('128.0.0.0'))

    def test_invalid_cidr_to_mask(self):
        self.assertEqual('Invalid', self.convert.cidr_to_mask('0.0'))

    def test_cidr_to_mask(self):
        self.assertEqual('Invalid', self.convert.cidr_to_mask('85'))

    def test_mask_to_cidr(self):
         self.assertEqual('24', self.convert.mask_to_cidr('255.255.255.0'))
         self.assertEqual('16', self.convert.mask_to_cidr('255.255.0.0'))
         self.assertEqual('8', self.convert.mask_to_cidr('255.0.0.0'))

         self.assertEqual('Invalid', self.convert.mask_to_cidr(''))
         self.assertEqual('Invalid', self.convert.mask_to_cidr('255.255.255.255.'))
         self.assertEqual('Invalid', self.convert.mask_to_cidr('0.0.0.0.'))
         self.assertEqual('Invalid', self.convert.mask_to_cidr('255.255.255.256'))

    def test_valid_ipv4(self):
        self.assertTrue(self.validate.validate_ip('127.0.0.1'))
        self.assertTrue(self.validate.validate_ip('127.0.0.1'))
        self.assertTrue(self.validate.validate_ip('192.168.0.1'))
        self.assertTrue(self.validate.validate_ip('10.0.0.1'))
        self.assertTrue(self.validate.validate_ip('172.16.0.1'))
        self.assertTrue(self.validate.validate_ip('255.255.255.255'))

    def test_invalid_ipv4(self):
        self.assertFalse(self.validate.validate_ip('192.168.1.2.3'))
        self.assertFalse(self.validate.validate_ip('192.168.1.2.3'))
        self.assertFalse(self.validate.validate_ip('192.168.0'))
        self.assertFalse(self.validate.validate_ip('10.0.0.256'))
        self.assertFalse(self.validate.validate_ip('172.32.0.1..'))
        self.assertFalse(self.validate.validate_ip(''))
        self.assertFalse(self.validate.validate_ip(None))


if __name__ == '__main__':
    unittest.main()
