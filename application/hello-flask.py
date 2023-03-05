from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Sweet Jesus! GitHub triggered CodePipeline. CodePipeline triggered CodeBuild. CodeBuild built image to ECR. Pipeline sent image to ECS. LoadBalancer says HELLLLLO!!!"

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=80)

