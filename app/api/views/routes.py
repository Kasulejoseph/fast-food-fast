from flask import Flask, request,jsonify,Blueprint
from flask_restful import Api, Resource
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
        all = ORDERS.get_all_order('detail')
        if all:
            return jsonify({'message': all}),200
        return jsonify({'error':'empty'}),404

    @main.route(
        '/api/v1/orders/',
        methods=['POST'])
    def add_order():
        data = request.get_json()
        detail = data.get('details')
        if detail:
            add = ORDERS.add_order(detail,id)
            return jsonify({'message': add }),201
        return jsonify({'error': 'errrror'}), 404


class OrderOne(Resource):
    """
    class for access order by its id
    """
    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['GET'])
    def get_order(id):
        one1 = ORDERS.get_one_order(id)
        if ORDERS.is_order_exist(id):
            return jsonify({'error': ORDERS.is_order_exist(id)}),404
        return jsonify({'message': one1}), 200
        

    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['PUT'])
    def update_order(id):
        data = request.get_json()
        detail = data.get('details')
        update = ORDERS.update_order(detail,id)
        if update:
            return jsonify({'message': update})

    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['DELETE'])
    def delete_order(id):
        pass


api.add_resource(OrderOne, 
    '/api/v1/order/<int:id>', endpoint='order')
api.add_resource(OrderAll,
    '/api/v1/order/', endpoint='orderall')
