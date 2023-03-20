from flask import jsonify, Flask, request, url_for, redirect
from flask_cors import CORS
from flask_restful import Api
from application.api.createcomic import CreateComic
from application.models import Comic
import application.models 
from application.extensions import db
from application.api.listcomics import ListComics
from application.api.getcomic import GetComic
from application.api.getlatest import GetLatest
from application.api.getalllatest import GetAllLatest

def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.DevelopmentConfig")
    CORS(app)
    api = Api(app)
    api.add_resource(ListComics, '/api/list-names/')
    api.add_resource(GetComic, '/api/comics/<id>/')
    api.add_resource(GetLatest, '/api/comics/name/<name>/')
    api.add_resource(GetAllLatest, '/api/comics/')
#    api.add_resource(CreateComic, '/comics/new/<name>')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

