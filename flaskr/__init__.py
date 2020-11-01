from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
import os

db = SQLAlchemy()
# login_manager = LoginManager()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.TestConfig')

    db.init_app(app)

    with app.app_context():
        from . import routes

        db.create_all()

        return app
