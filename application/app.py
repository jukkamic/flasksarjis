from flask import jsonify, Flask
from flask_cors import CORS
from .parsers.parser import Parser
from .models import Comic
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from .models import Base

engine = create_engine('postgresql://postgres:secret@database-5432-tcp', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.Config")
    CORS(app)

    @app.route('/')
    def index():
        return "Sweet Jesus v4.1.SQLAlchemy! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this). No time for templates! All SQLAlchemy and no play makes Flask a dull toy. It works. It doesn't work. It works? ... WE CONFIRM: Database and HTTP server have been separated. They have been separated."

    @app.route('/list-names', methods = ['GET'])
    def getNames():    
        session = Session()
        comics = session.query(Comic).all()
        return jsonify(comics)

    @app.route('/create/<name>', methods = ['GET'])
    def createComic(name:str):
        session = Session()
        with session:    
            comic = Comic(name=name, display_name="testing name")
            session.add(comic)
            session.commit()
        return "Thanks a lot!"

    return app
