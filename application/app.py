from flask import Flask, jsonify
from .models import db 
from .parsers.parser import Parser

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sarjis.db'
db.init_app(app)

@app.route('/')
def index():
    return "Sweet Jesus! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this)"

@app.route('/list-names', methods = ['GET'])
def getNames():    
    return jsonify(Parser.getComicNames())

if __name__ == '__main__':
    app.run(debug=True)
    

