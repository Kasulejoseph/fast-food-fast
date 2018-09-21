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

    def test_get_order_when_no_orders_in_order_list(self):
        list = []
        result = self.client.get('/api/v1/orders/',
                    content_type = 'application/json',
                    data  = json.dumps(list))

        self.assertEqual(result.status,'404 NOT FOUND')
        self.assertIn('no orders posted yet',str(result.data))
        
    def test_request_get_all_orders(self):
        self.list = [{
            'id':3 ,
            'dish': "jgh",
            'description': "description",
            'price': 34
        }]
        result = self.client.get('/api/v1/orders/',
                    content_type = 'application/json',
                    data = json.dumps(self.list)
        )
        data = json.loads(result.data.decode())
        self.assertEqual(result.status,'200 OK')
        self.assertTrue(result)
        self.assertIsInstance(data['Orders'], list)
        self.assertTrue(len(data['Orders']) != 0)
        self.assertIn('"price": 34',str(result.data))

    def test_can_get_order_by_id(self):
        self.list = [{
            'id':3 ,
            'dish': "jgh",
            'description': "description",
            'price': 34
        }]
        result = self.client.get('/api/v1/orders/1',
                    content_type ='aplication/json',
                    )
        data = json.loads(result.data.decode())
        self.assertEqual(result.status_code,404)
        #self.assertIn("bad request, order not found",str(result.data))

