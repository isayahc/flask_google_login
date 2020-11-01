"""Data models."""
from datetime import datetime
from . import db


class User(db.Model):
    '''username, pw_has'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pw_hash = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)
