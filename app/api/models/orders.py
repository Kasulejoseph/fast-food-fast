from flask import json
from app.api.models.dish import Order

class OrderList:
    """
    data structures
    """
    def __init__(self):
        self.order_list = []

    def is_order_exist(self, id):
        for order in self.order_list:
            if order['id'] != id:
                return "bad request, order not found"

    def add_order(self,order_data,id):
        """
        create an order in not exists
        """
        details = order_data
        order = Order(id,details['dish'],details['description'],details['price'])
        order_dict = order.order_json()
        if order_dict in self.order_list:
            return "Order already exist"
        else:
            self.order_list.append(order_dict)
            return order_dict

    def get_all_order(self, order_data):
        """
        get all orders posted
        """
        details = order_data
        if self.order_list is not None:
            return self.order_list
        return "order list empty"

    def get_one_order(self,id):
        pass

    def update_order(self,details,id):
        pass

    def delete_one_order(self, id):
        pass

        
        

    
