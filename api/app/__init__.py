from flask import Flask 
from app.api.views.routes import main
from app.config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config["development"])
app.register_blueprint(main)