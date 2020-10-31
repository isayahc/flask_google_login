from enum import unique
# from flaskr import create_app, db, login_manager
from flask_login import UserMixin
from datetime import datetime
from . import db
# from flask_sqlalchemy import SQLAlchemy


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))

    def __init__(self, username, pw_hash) -> None:
        self.username = username
        self.pw_hash = pw_hash

    # CRUD BOIII

    # create
    @staticmethod
    def create(username, pw_hash):
        # make sure is unique
        user = User(
            username=username,
            pw_hash=pw_hash
        )
        db.session.add(user)
        db.session.commit()

    # read
    @staticmethod
    def get(user_id: int):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return None
        else:
            return user


# def init_db(app = create_app()):
#     db.create_all()

#     # Create a test user
#     new_user = User('a@a.com', 'aaaaaaaa')
#     new_user.display_name = 'Nathan'
#     db.session.add(new_user)
#     db.session.commit()

#     new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
#     db.session.commit()
