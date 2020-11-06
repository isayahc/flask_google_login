"""Data models."""
from flask_login import UserMixin
from . import db, login_manager


class User(db.Model, UserMixin):
    '''username, pw_has'''
    __tablename__ = "users"
    id_ = db.Column(
        db.Integer,
        primary_key=True
        )

    name = db.Column(
        db.String(80),
        nullable=False
        )

    email = db.Column(
        db.String(80),
        nullable=False,
        unique=True
        )

    profile_pic = db.Column(
        db.String(80),
        nullable=False,
        unique=True,
        index=False
        )

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def get(email: str):
        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def create(name, email, profile_pic):
        user = User(name=name, email=email, profile_pic=profile_pic)
        db.session.add(user)
        db.session.commit()

    def get_id(self):
        return (self.id_)

    def is_authenticated(self):
        return True

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(user_id)
        except:
            return None
