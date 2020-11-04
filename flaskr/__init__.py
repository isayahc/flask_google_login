# 3rd party libraries

# Flask specific library
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# flask util
login_manager = LoginManager()
db = SQLAlchemy()

# google API Data


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    from .model import db

    db.init_app(app)
    db.app = app
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message = "NICE!"

    with app.app_context():
        from . import routes

        db.create_all()

        return app
