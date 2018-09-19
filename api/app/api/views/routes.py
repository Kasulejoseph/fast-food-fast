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
        data = request.get_json()
        detail = data.get('details')
        if ORDERS.is_valid_order(detail):
            return jsonify({'error': ORDERS.is_valid_order(detail)}), 404
        add = ORDERS.add_order(detail,id)
        return jsonify({'order': add }),201


class OrderOne(Resource):
    """
    class for access order by its id
    """
    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['GET'])
    def get_order(id):
        one1 = ORDERS.get_one_order(id)
        if not ORDERS.is_order_exist(id):
            return jsonify({'error': ORDERS.is_order_exist(id)}),404
        return jsonify({'message': one1}), 200
        
    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['PUT'])
    def update_order(id):
        data = request.get_json()
        detail = data.get('details')
        update = ORDERS.update_order(detail,id)
        if len(detail) !=4:
            abort(404)
        if update:
            return jsonify({'message': update})

    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['DELETE'])
    def delete_order(id):
        if not ORDERS.is_order_exist(id):
            return jsonify({'error': ORDERS.is_order_exist(id)}),404
        delete_one = ORDERS.delete_one_order(id)
        return jsonify({'message': delete_one}), 200


api.add_resource(OrderOne, 
    '/api/v1/order/<int:id>', endpoint='order')
api.add_resource(OrderAll,
    '/api/v1/order/', endpoint='orderall')
