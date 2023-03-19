from flask_restful import Resource
from application.models import Comic
from flask import jsonify

class GetComic(Resource):

    def get(self, id):
        comic = Comic.get_comic_by_id(id)
        return comic.json()
    