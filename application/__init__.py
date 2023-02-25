from flask import Flask
from flask_management_endpoints import z_blueprint

app = Flask(__name__)
app.register_blueprint(z_blueprint, url_prefix='')

from application import routes

