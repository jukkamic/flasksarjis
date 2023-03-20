import json
#import logging
from application.models import Comic, NotFoundException
from flask import jsonify
from application.parsers.hs import HsParser
from application.parsers.luonto import LuontoParser
from application.parsers.redmeat import RedmeatParser
from application.parsers.smbc import SmbcParser
from application.parsers.pbf import PbfParser
from application.parsers.xkcd import XkcdParser

#log = logging.getLogger('sarjis')

class Parser():

    comicSources:any = [
            {
                "name": "fingerpori",
                "displayName": "Fingerpori",
                "title": "Fingerpori",
                "parser": HsParser
            },
            {
                "name": "vw",
                "displayName": "Viivi ja Wagner",
                "title": "Viivi ja Wagner",
                "parser": HsParser
            },
            {
                "name": "luonto",
                "displayName": "Kamala luonto",
                "title": "Kamala luonto",
                "parser": LuontoParser
            },
            {
                "name": "xkcd",
                "displayName": "xkcd",
                "title": "",
                "parser": XkcdParser
            },
            {
                "name": "smbc",
                "displayName": "Saturday Morning Breakfast Cereal",
                "title": "",
                "parser": SmbcParser
            },
            {
                "name": "fokit",
                "displayName": "Fok_It",
                "title": "Fok_It",
                "parser": HsParser
            },
            {
                "name": "redmeat",
                "displayName": "Red Meat",
                "title": "Red Meat",
                "parser": RedmeatParser
            },
            {
                "name": "pbf",
                "displayName": "The Perry Bible Fellowship",
                "title": "",
                "parser": PbfParser
            }
        ]

    @staticmethod
    def parse(name:str, path:str):
        for source in Parser.comicSources:
            if source['name'] == name:
                try:
                    # logging.debug("Trying to use parser '%s' from path '%s' with title '%s'", source['parser'], path, source['title'])
                    ret = source['parser'].parse(path, source['title'])            
                    ret['name'] = name
                except Exception as e:
                    # logging.debug("Error parsing source: {}".format(e))
                    return json.dumps({"message": e.message})
                # logging.debug("Returning parsed comic")
                return ret
        return jsonify({"content": "No parser found for requested comic: " + name})

    @staticmethod
    def getComicNames():
        names = []
        for source in Parser.comicSources:
            names.append({'name': source['name'], 'displayName': source['displayName']})
        return names
    
    @staticmethod    
    def updateLinks(name:str, comic:any):
        # logging.debug("update links for {}".format(name))
        if comic is None:
            raise Exception("updateLinks: comic is None")
        if not comic.prev_link:
            # logging.info("Comic {} \n has no predecessor.".format(comic.name))
            return comic.json()
        else:
            # fetch prev, add current id as next, update prev_id for current
            prev_comic:Comic=None
            try:
                prev_comic = Comic.get_comic_by_permalink(comic.prev_link)
                prev_comic.next_id = comic.id
                # logging.debug("Saving prev_comic: {}".format(prev_comic.name))
                prev_comic.save()
                # if prev_comic is not None:
                    # logging.debug("save() returned {}".format(prev_comic.name))
                # else:
                    # logging.debug("save() returned None")
            except NotFoundException:
                # logging.debug("Comic not found from database by prev_link {}. Parsing it from web.".format(comic.prev_link))
                prev_comic_dict = Parser.parse(name, comic.prev_link)
                # logging.debug("Previous comic parsed: {}".format(prev_comic_dict['name']))
                # logging.debug("Creating new Comic from prev_comic_dict of type ", type(prev_comic_dict))
                prev_comic = Comic(prev_comic_dict)
                prev_comic.save()
                # logging.debug("Saved prev_comic that was parsed from web")
            # logging.debug("Why would prev_comic.id exist? {} " .format(prev_comic.id))
            comic.prev_id = prev_comic.id
            comic.save()
            return comic.json()
