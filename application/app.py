from flask import jsonify, Flask, request
from flask_cors import CORS
from .parsers.parser import Parser
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comic(db.Model):
    __tablename__ = 'comics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.display_name!r})"
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def create_app():
    app = Flask(__name__)
    app.config.from_object("application.config.Config")
    CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return "Sweet Jesus v4.1.SQLAlchemy! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this). No time for templates! All SQLAlchemy and no play makes Flask a dull toy. It works. It doesn't work. It works? ... WE CONFIRM: Database and HTTP server have been separated. They have been separated."

    @app.route('/list-names', methods = ['GET'])
    def getNames():    
        comics = db.session.execute(db.select(Comic)).scalars()
        for comic in comics:
            print( "comic " + comic.name)
        return "Lots of them"

    @app.route('/create/<name>', methods = ['GET'])
    def createComic(name:str):
        comic = Comic(name=name, display_name="testing name")
        db.session.add(comic)
        db.session.commit()
        return "Thanks a lot!"
    
    @app.route('/comics/id/<int:id>/', methods= ['GET'])
    def getComic(id):
        comic = db.get(Comic, id)
        return jsonify(comic)
        
    return app

