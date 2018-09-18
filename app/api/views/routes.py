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
        pass

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
        pass
        

    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['PUT'])
    def update_order(id):
        pass

    @main.route(
        '/api/v1/orders/<int:id>',
        methods=['DELETE'])
    def delete_order(id):
        pass


api.add_resource(OrderOne, 
    '/api/v1/order/<int:id>', endpoint='order')
api.add_resource(OrderAll,
    '/api/v1/order/', endpoint='orderall')
