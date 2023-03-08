import unittest
from unittest.mock import patch, MagicMock
from methods import *


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.restricted = Restricted()
        self.token = Token()
   

    @patch('builtins.print')
    def test_generate_token_success(self, mock_print):
        query_result = [('salt', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', 'admin')]
        expected_token = self.token.generateToken('admin', 'secret', query_result)
        self.assertIsNotNone(expected_token)

    def test_generate_token_failure(self):
        query_result = [('salt', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', 'admin')]
        with self.assertRaises(ValueError):
            self.token.generateToken('admin', 'wrongpassword', query_result)

        
    def test_access_data(self):
        result = self.restricted.access_Data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.BmcZ8aB5j8wLSK8CqdDwkGxZfFwM1X1gfAIN7cXOx9w')
        self.assertEqual('Access Granted', result)

    def test_access_data_valid_token(self):
        authorization_header = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI' 
        self.assertEqual('Access Granted', self.restricted.access_Data(authorization_header))

    def test_access_data_invalid_token(self):
        result = self.restricted.access_Data('invalid_token')
        self.assertFalse(result)

    def test_access_data_missing_token(self):
        result = self.restricted.access_Data(None)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
