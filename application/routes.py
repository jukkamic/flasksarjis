from application import app

@app.route('/')
def index():
    return "Hello, Flask 02:01!"
