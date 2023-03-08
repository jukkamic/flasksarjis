import json

class Parser():

    comicSources:any = [
            {
                "name": "fingerpori",
                "displayName": "Fingerpori",
                "title": "Fingerpori",
                "parser": "HsParser"
            },
            {
                "name": "vw",
                "displayName": "Viivi ja Wagner",
                "title": "Viivi ja Wagner",
                "parser": "HsParser"
            },
            {
                "name": "luonto",
                "displayName": "Kamala luonto",
                "title": "Kamala luonto",
                "parser": "LuontoParser"
            },
            {
                "name": "dilbert",
                "displayName": "Dilbert",
                "title": "",
                "parser": "DilbertParser"
            },
            {
                "name": "xkcd",
                "displayName": "xkcd",
                "title": "",
                "parser": "XkcdParser"
            },
            {
                "name": "smbc",
                "displayName": "Saturday Morning Breakfast Cereal",
                "title": "",
                "parser": "SmbcParser"
            },
            {
                "name": "fokit",
                "displayName": "Fok_It",
                "title": "Fok_It",
                "parser": "HsParser"
            },
            {
                "name": "redmeat",
                "displayName": "Red Meat",
                "title": "Red Meat",
                "parser": "RedmeatParser"
            },
            {
                "name": "pbf",
                "displayName": "The Perry Bible Fellowship",
                "title": "",
                "parser": "PbfParser"
            },
            # {
            #     "name": "velho",
            #     "title": "Velho",
            #     "parser": HsParser
            # }
        ]

    @staticmethod
    def parse(name:str, path:str):
        for source in Parser.comicSources:
            if source['name'] == name:
                try:
                    ret = source['parser'].parse(path, source['title'])            
                except Exception as e:
                    return json.dumps({"message": str(e)})
                return ret
        return json.dumps({"content": "No parser found for requested comic: " + name})

    @staticmethod
    def getComicNames():
        names = []
        for source in Parser.comicSources:
            names.append({'name': source['name'], 'displayName': source['displayName']})
        return names