from flask import flask

def create_app():
    app = flask.Flask(__name__)
    app.config['SECRET_KEY'] = 'practicasUTCH'
    return app