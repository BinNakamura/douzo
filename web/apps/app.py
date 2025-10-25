from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello from Flask via uWSGI + nginx!"

    return app
