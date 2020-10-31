from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
import os

db = SQLAlchemy()
# login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # from flaskr.models import User
        db.init_app(app)
        db.create_all()
        # db.create_all()
        if not db.app:
            raise 'wtf'

    return app
        # print('hello')
    #     from .models import User
    #     db.init_app(app)
    #     login_manager.init_app(app)
    
    # db.create_all(app=app)
    # user = User('j', 'j')
    # db.session.add(user)
    # db.session.commit()
    # print(user)


    # return app

app = create_app()
print(db.app())
