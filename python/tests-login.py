import unittest
from unittest.mock import patch, MagicMock
from methods import *

login = Token()

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.restricted = Restricted()
        self.token = Token()
    
    def test_access_data_valid_credentials(self):
        # Generate a valid token using existing method
        login = Login()
        token = login.generateToken('admin', 'secret')

        # Ensure access to protected data with valid token and credentials
        result = self.restricted.access_Data(token, 'admin', 'secret')
        self.assertEqual('You are under protected data', result)


    def test_access_data(self):
        result = self.restricted.access_Data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w')
        self.assertEqual('You are under protected data', result)

    def test_access_data_valid_token(self):
        authorization_header = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI' 
        self.assertEqual('You are under protected data', self.restricted.access_Data(authorization_header))

    def test_access_data_invalid_token(self):
        result = self.restricted.access_Data('invalid_token')
        self.assertFalse(result)

    def test_access_data_missing_token(self):
        result = self.restricted.access_Data(None)
        self.assertFalse(result)

    def test_access_data_expired_token(self):
        authorization_header = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.8Zs_lT7V1wzTfbKM7mPbF-BRYE9GJbLj1Y7VzsZsASw'
        self.assertFalse(self.restricted.access_Data(authorization_header))

    def test_access_data_invalid_signature(self):
        authorization_header = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.invalid_signature'
        self.assertFalse(self.restricted.access_Data(authorization_header))

    def test_access_data_invalid_header(self):
        authorization_header = 'InvalidHeader eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.8Zs_lT7V1wzTfbKM7mPbF-BRYE9GJbLj1Y7VzsZsASw'
        self.assertFalse(self.restricted.access_Data(authorization_header))

    def test_access_data_missing_bearer_prefix(self):
        authorization_header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.8Zs_lT7V1wzTfbKM7mPbF-BRYE9GJbLj1Y7VzsZsASw'
        self.assertFalse(self.restricted.access_Data(authorization_header))

    def test_access_data_wrong_role(self):
        authorization_header = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SYsOQbk-Nx0xJ9ss9rv_9L-6aOcJ-vpU6MJ_GbthYiw'
        self.assertFalse(self.restricted.access_Data(authorization_header))

if __name__ == '__main__':
    unittest.main()
