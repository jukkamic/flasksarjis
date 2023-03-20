from flask_restful import Resource
from flask import jsonify
from application.models import Comic, NotFoundException
from application.parsers.parser import Parser
from application.config import Config
import logging

# logging.config.dictConfig(Config.LOGGING)
# log = logging.getLogger('sarjis')

class GetLatest(Resource):
    def get(self, name:str):
        # logging.debug("********* GetLatest: {}".format(name))
        comic_json = Parser.parse(name, "/")
        if (type(comic_json) is str):
            raise Exception("comic_json is a string!", comic_json)
        # comic_json['name'] = name
        try:
            # log.debug("COMIC_JSON IS TYPE", type(comic_json))
#            logging.debug("perm_link is ", comic_json['perm_link'])
            link = comic_json["perm_link"]
            # log.debug("link is ", link)
            comic_from_db = Comic.get_comic_by_permalink(link)
            # logging.debug("comic_from_db: {}".format(comic_from_db.name))
            return comic_from_db.json()
        except NotFoundException:
            # logging.debug("Not found, creating new comic")
            comic = Comic(comic_json)
            comic.save()
            return Parser.updateLinks(name, comic)
