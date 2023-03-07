import json

class Parser():

    comicSources:any = [
            {
                "name": "fingerpori",
                "title": "Fingerpori",
                "parser": "HsParser"
            },
            {
                "name": "vw",
                "title": "Viivi ja Wagner",
                "parser": "HsParser"
            },
            {
                "name": "luonto",
                "title": "Kamala luonto",
                "parser": "LuontoParser"
            },
            {
                "name": "dilbert",
                "title": "",
                "parser": "DilbertParser"
            },
            {
                "name": "xkcd",
                "title": "",
                "parser": "XkcdParser"
            },
            {
                "name": "smbc",
                "title": "",
                "parser": "SmbcParser"
            },
            {
                "name": "fokit",
                "title": "Fok_It",
                "parser": "HsParser"
            },
            {
                "name": "redmeat",
                "title": "Red Meat",
                "parser": "RedmeatParser"
            },
            {
                "name": "pbf",
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
            names.append({'name': source['name']})
        return names