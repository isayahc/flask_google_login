# 3rd party libraries
import json

# Flask specific library
from flask import Flask, request
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

    with app.app_context():
        from . import routes
    
        db.create_all()

        return app
