"""Data models."""
from datetime import datetime
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))

    def __repr__(self):
        return "<User {}>".format(self.username)
