from flask import jsonify, Flask
from flask_cors import CORS
from .parsers.parser import Parser
from .models import Comic
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from .models import Base

engine = create_engine('mariadb://root:mariarootp@sarjis/sarjis', echo=True)
Base.metadata.create_all(engine)

def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.Config")
    CORS(app)

    @app.route('/x')
    def index():
        return "Sweet Jesus v4.0.SQLAlchemy! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this). No time for templates! All SQLAlchemy and no play makes Flask a dull toy. It works. It doesn't work. It works?"

    @app.route('/list-names', methods = ['GET'])
    def getNames():    
        return jsonify(Parser.getComicNames())

    @app.route('/create/<int:id>/<name>', methods = ['GET'])
    def createComic(id:int, name:str):
        with Session(engine) as session:    
            comic = Comic(id=id, name=name, display_name="testing name")
            session.add(comic)
            session.commit()
        return "Thanks a lot!"

    return app
