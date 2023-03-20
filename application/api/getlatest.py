from flask_restful import Resource
from application.models import Comic, NotFoundException
from application.parsers.parser import Parser
import logging

class GetLatest(Resource):
    def get(self, name:str):
        logging.debug("********* GetLatest: %s", name)
        comic_json = Parser.parse(name, "/")
        comic_json['name'] = name
        try:
            comic_from_db = Comic.get_comic_by_permalink(comic_json['perm_link'])
            logging.debug("comic_from_db: ", comic_from_db)
            return comic_from_db.json()
        except NotFoundException:
            logging.debug("Not found, creating new comic")
            comic = Comic(comic_json)
            comic.save()
            return Parser.updateLinks(name, comic)
