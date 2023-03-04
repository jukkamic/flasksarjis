from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! GitHub triggered build. Pipeline triggered deployment. V4."

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=80)

