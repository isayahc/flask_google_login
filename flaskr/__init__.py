from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    return app

