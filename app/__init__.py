from flask import Flask 
from app.api.views.routes import main
app = Flask(__name__)
app.register_blueprint(main)