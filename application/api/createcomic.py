from flask_restful import Resource
from application.models import Comic

class CreateComic(Resource):
        
    def get(self, name:str):
        comic = Comic(name=name, display_name="testing name")
        comic.save()
        return "Thanks a lot!"
