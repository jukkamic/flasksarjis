from flask_restful import Resource
from application.models import Comic
from flask import jsonify
from application.parsers.parser import Parser
import logging

class GetComic(Resource):
    
    def get(self, id):
        logging.debug("Get comic {}".format(id))
        comic = Comic.get_comic_by_id(id)
        if comic is None:
            raise Exception("Comic not found")
        if (comic.prev_id is not None):
            return comic.json()
        else:
            logging.debug("Comic.prev_id is None, updating links")
            return Parser.updateLinks(comic.name, comic)

    