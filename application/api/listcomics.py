from application.models import Comic
from flask import jsonify
from flask_restful import Resource
from application import app

class ListComics(Resource):

    # def get(self):
    #     return "Sweet Jesus v4.1.SQLAlchemy! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this). No time for templates! All SQLAlchemy and no play makes Flask a dull toy. It works. It doesn't work. It works? ... WE CONFIRM: Database and HTTP server have been separated. They have been separated."

    def get(self):    
        return {
            'comics': [comic.json() for comic in Comic.query.all()]} 


