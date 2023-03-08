from flask import jsonify, Flask
from flask_cors import CORS
from .parsers.parser import Parser
from .models import Comic

def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.Config")
    CORS(app)

    comic = Comic()

    @app.route('/')
    def index():
        return "Sweet Jesus v3.0.SQLAlchemy! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this). No time for templates! All SQLAlchemy and no play makes Flask a dull toy. It works. It doesn't work. It works?"

    @app.route('/list-names', methods = ['GET'])
    def getNames():    
        return jsonify(Parser.getComicNames())
    
    return app
