from flask import jsonify, Flask, request
from flask_cors import CORS
from flask_restful import Api
from application.api.createcomic import CreateComic
from application.extensions import db
from application.models import Comic
from application.api.listcomics import ListComics
from application.api.getcomic import GetComic

def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.DevelopmentConfig")
    CORS(app)
    api = Api(app)
    api.add_resource(ListComics, '/')
    api.add_resource(GetComic, '/comics/<id>')
    api.add_resource(CreateComic, '/comics/new/<name>')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


