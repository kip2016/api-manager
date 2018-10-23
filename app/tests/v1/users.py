import unittest
import json
from flask import Flask 
from app import create_app
from app import tests


class test_client(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    
    def test_user_login_status_code(self):
        result = self.client.get('/api/v1/login')
        self.assertEqual(result.status_code,401)

    