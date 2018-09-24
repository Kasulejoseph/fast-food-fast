from flask import Flask, request,jsonify,Blueprint
from flask_restful import Api, Resource, abort
from app.api.models.orders import OrderList
from app.api import app

main = Blueprint('main', __name__)
api = Api(app)
ORDERS = OrderList()

class OrderAll(Resource):
    """
    Get all orders
    """
    @main.route(
        '/api/v1/orders/',
        methods=['GET'])
    def get_all():
        all = ORDERS.get_all_order()
        if all:
            return jsonify({'Orders': all}),200
        return jsonify({'error':'no orders posted yet'}),404

    @main.route(
        '/api/v1/orders/',
        methods=['POST'])
    def add_order():
        if not request.content_type == 'application/json':
            return jsonify({"failed": 'Content-type must be application/json'}), 401
        
        data = request.get_json()
        detail = data.get('details')

        if not data:
            return jsonify({'failed': 'Details keyword and attributes not specified in the request'}), 401
        
        if not detail:
            return jsonify({'failed': 'Details keyword has no attributes specified in the request'}), 400

        if ORDERS.is_valid_order(detail):
            return jsonify({'error': ORDERS.is_valid_order(detail)}), 404
        add = ORDERS.add_order(detail,id)
        return jsonify({'order': add }),201


class OrderOne(Resource):
    """
    class combines all methods that accept order requests by their ids
    """
    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['GET'])
    def get_order(id):
        #Call get_one_order in ORDERS class to verify the requested id
        one1 = ORDERS.get_one_order(id)

        order_exist = ORDERS.is_order_exist(id)
        if not order_exist:
            return jsonify({'error': order_exist}),404
        
        if not one1:
            return jsonify({"invalid":"order id requested not found"}),400
        return jsonify({'message': one1}), 200
        
    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['PUT'])
    def update_order(id):
        if not request.content_type == 'application/json':
            return jsonify({"failed": 'Content-type must be application/json'}), 401
        
        #Get request in json format
        data = request.get_json()
        detail = data.get('details')
        one1 = ORDERS.get_one_order(id)

        if not data:
            return jsonify({'failed': 'No attributes specified in the request'}), 401
        
        if not one1:
            return jsonify({"invalid":"No content found for requested it"}),400
        
        if len(detail) !=5:
            abort(404)
    
        #Call update_orders in ORDERS which updates the order status
        update = ORDERS.update_order(detail,id)
        if update:
            return jsonify({'message': update}),200

    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['DELETE'])
    def delete_order(id):
        #Call is_order_exist to confirm whether the passed id is a valid
        order_exist = ORDERS.is_order_exist(id)
        if not order_exist:
            return jsonify({'error': order_exist}),404

        #Call ORDERS.delete_one_order(id) to delete the order by id
        delete_one = ORDERS.delete_one_order(id)
        if not delete_one:
            return jsonify({"failed": "order id to delete not found"}),401
        return jsonify({'message': delete_one}), 200


api.add_resource(OrderOne, 
    '/api/v1/order/<int:id>', endpoint='order')
api.add_resource(OrderAll,
    '/api/v1/order/', endpoint='orderall')
