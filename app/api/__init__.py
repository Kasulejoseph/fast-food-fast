from flask import Flask, Blueprint
from flask_restful import Api, Resource, abort
from app.api.models.orders import OrderList
from app.api.views.routes import OrderOne, OrderAll

main = Blueprint('main', __name__)
food_api = Api(main)


food_api.add_resource(OrderOne, '/api/v1/orders/<int:id>')
food_api.add_resource(OrderAll, '/api/v1/orders/')

