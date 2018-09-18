from flask import Flask, Blueprint
app = Flask(__name__)
main = Blueprint('main', __name__)