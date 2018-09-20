from tests.test_base import BaseTestCase
from app.api.models.orders import OrderList

import unittest
import json

class TestOrderRoutes(BaseTestCase):

    def test_order_creation(self):
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,201)

    def test_no_details_keyword_in_order_request(self):
        self.order = {}
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,401)
        self.assertIn('Details keyword and attributes not specified in the request',str(result.data))
    
    def test_no_content_in_order_request(self):
        self.order = { 'details':{}}
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,400)
        self.assertIn('Details keyword has no attributes specified in the request',str(result.data))
    
    def test_order_can_be_added_to_list_of_orders(self):
        self.list = []
        self.order = {'details': {
            'id':3 ,
            'dish': "jgh",
            'description': "description",
            'price': 34
        }}
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.list.append(self.order)
        self.assertEqual(result.status_code,201)
        self.assertIn("description",str(result.data))

    def test_request_not_json(self):
        result = self.client.post('/api/v1/orders/',
                    content_type = 'text/css',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,401)
        self.assertIn('Content-type must be application/json',str(result.data))



if __name__ == '__main__':
    unittest.main()