import unittest
import json
from flask import Flask 
from app import create_app
from app import tests
sales_orders = [{
    "id":1,
    "name":"pizza",
    "description":"small",
    "price":800
    
}]

class test_client(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        

    def test_post_sales(self):
        result = self.client.post('/api/v1/sales',data=json.dumps(sales_orders[0]),content_type='application/json')
        res = json.loads(result.data.decode())
        self.assertEqual(res['Message'],"Post Success")
        self.assertEqual(res['Status'],"Ok")
        self.assertEqual(result.status_code,201)

    def test_sales_status_code(self):
        result = self.client.get('/api/v1/sales')
        self.assertEqual(result.status_code,200)

    def test_single_sale_status_code(self):
        result = self.client.get('/api/v1/sales/1')
        self.assertEqual(result.status_code,200)


