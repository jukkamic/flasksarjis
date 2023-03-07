from flask import jsonify, Flask
from .parsers.parser import Parser
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.Config")

    @app.route('/')
    def index():
        return "Sweet Jesus! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this)"

    @app.route('/list-names', methods = ['GET'])
    def getNames():    
        return jsonify(Parser.getComicNames())
    
    return app
