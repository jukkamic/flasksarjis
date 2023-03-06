from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Sweet Jesus! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!! ****AND NOW WITH WSGI**** (gonna need an html template for this)"

