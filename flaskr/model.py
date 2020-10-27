from flaskr import db


class User(db.Model):
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))

    def __init__(self, username, pw_hash) -> None:
        self.username = username
        self.pw_hash = pw_hash
