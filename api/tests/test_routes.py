from tests.test_base import BaseTestCase
from app.api.models.orders import OrderList

import unittest
import json

class TestOrderRoutes(BaseTestCase):
    """ 
    Test case to test end points
    :routes.py
    """

    def test_order_creation(self):
        """ Test status code whenever order is created """
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,201)

    def test_no_details_keyword_in_order_request(self):
        """ Test detail keyword is not passed with the order post """
        self.order = {}
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,401)
        self.assertIn('Details keyword and attributes not specified in the request',str(result.data))
    
    def test_no_content_in_order_request(self):
        """ Test detail keyword is passed but with
            empty content or order item
        """
        self.order = { 'details':{}}
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,400)
        self.assertIn('Details keyword has no attributes specified in the request',str(result.data))
    
    def test_order_can_be_added_to_list_of_orders(self):
        """ Test order can be appended to order lists """
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
        """ Test order content to be posted not in json format """
        result = self.client.post('/api/v1/orders/',
                    content_type = 'text/css',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,401)
        self.assertIn('Content-type must be application/json',str(result.data))

    def test_get_order_when_no_orders_in_order_list(self):
        """ Test can't get orders when their is no food items available """
        list = []
        result = self.client.get('/api/v1/orders/',
                    content_type = 'application/json',
                    data  = json.dumps(list))

        self.assertEqual(result.status,'404 NOT FOUND')
        self.assertIn('no orders posted yet',str(result.data))
        
    def test_request_get_all_orders(self):
        """ Test can fetch all orders """
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

    def test_update_not_in_json(self):
        result = self.client.put('/api/v1/orders/1',
                    content_type = 'text/css',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,401)
        self.assertIn('Content-type must be application/json',str(result.data))

    def test_update_has_no_details_keyword_in_order_request(self):
        """ Test whether update request has detail keyword
            passed with the order post 
        """
        self.order = {}
        result = self.client.put('/api/v1/orders/1',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.assertEqual(result.status_code,401)
        self.assertIn('No attributes specified in the request',str(result.data))

    def test_id_has_no_corresponding_data(self):
        """ Test can't update a non existing order item """
        result = self.client.put('/api/v1/orders/2',
                    content_type = 'application/json',
                    data = json.dumps(self.order))

        self.assertEqual(result.status_code,400)
        self.assertIn("No content found for requested it", str(result.data))
    
    def test_incoming_update_is_valid(self):
        self.list = []
        self.order = {'details': {
            'dish': "jgh",
            'description': "description",
            'price': 34
        }}
        new =  {'details': {
            'dish': "jgh",
            'description': "description",
            'price': 34
        }}
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))
        self.list.append(self.order)
        data = json.loads(result.data.decode())
        self.assertEqual(result.status_code,201)
        #self.assertIn("peasd",str(data))
        self.assertIn("description",str(result.data))
        
        rs = self.client.put('/api/v1/orders/23',
                    content_type = 'application/json',
                    data= json.dumps(new))

        #data = json.loads(rs.data.decode())
        self.assertTrue(len(data['order']) ==5)
        self.assertTrue(data['order']['status'] == 'pending')
        self.assertIn('pending',str(data['order']))
        self.assertEqual(rs.status_code,404)

    # def test_order_can_be_updated(self):
    #     pass
    def test_cant_delete_food_item_when_food_list_empty(self):
        """ 
        A request to delete a food item
        from an empty food item list fails
        """
        rs = self.client.delete('/api/v1/orders/4',
                content_type = 'application/json',
                data = json.dumps(self.order))

        self.assertEqual(rs.status_code,404)
        self.assertIn("null",str(rs.data))

    def test_to_delete_order_by_invalid_id(self):
        """
        Trying to delete a food item from order list with 
        invalid id fails
        :id = 1000
        """
        self.list = []
        self.order = {'details': {
            'dish': "jgh",
            'description': "description",
            'price': 34
        }}
        #first post to the list
        result = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(self.order))

        #append to list and test for post         
        self.list.append(self.order)
        data = json.loads(result.data.decode())
        self.assertEqual(result.status_code,201)
        self.assertIn("description",str(result.data))

        #try to delete item with id 1000 that dont exist in the list
        rs = self.client.delete('/api/v1/orders/1000',
                content_type = 'application/json',
                data = json.dumps(self.order))
        #tests
        self.list.remove(self.order)
        self.assertEqual(rs.status_code,401)
        self.assertIn("order id to delete not found",str(rs.data))

    def test_kasule_deleted_by_id(self):
        """
        Delete order item by its id
        :id =23
        """
        list = []
        order = {'details': {
            'dish': "jgh",
            'description': "description",
            'price': 34
        }}
        #first post to the list
        rv = self.client.post('/api/v1/orders/',
                    content_type = 'application/json',
                     data=json.dumps(order))

        #append to list and test for post         
        list.append(order)
        data = json.loads(rv.data.decode())
        self.assertEqual(rv.status_code,201)
        self.assertIn("description",str(rv.data))

        #delete the food item by its id 23
        rs = self.client.delete('/api/v1/orders/23',
                content_type = 'application/json',
                data = json.dumps(order))
        #tests
        list.remove(order)
        self.assertEqual(rs.status_code,200)
        self.assertIn("deleted",str(rs.data))
        

        
