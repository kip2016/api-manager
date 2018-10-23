import unittest
import json
from flask import Flask 
from app import create_app
from instance.config import app_config
from app import tests
products_orders = [{
    "id":1,
    "name":"Jean trouser",
    "description":"black",
    "price":1500
    
}]


class test_client(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        

    def test_post_products(self):
        result = self.client.post('/api/v1/products',data=json.dumps(products_orders[0]),content_type='application/json')
        res = json.loads(result.data.decode())
        self.assertEqual(res['Message'],"Post Success")
        self.assertEqual(res['Status'],"Ok")
        self.assertEqual(result.status_code,201)

    def test_products_status_code(self):
        result = self.client.get('/api/v1/products')
        self.assertEqual(result.status_code,200)


    def test_single_product_status_code(self):
        result = self.client.get('/api/v1/products/1')
        self.assertEqual(result.status_code,200)