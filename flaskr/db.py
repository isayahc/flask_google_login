import sqlalchemy
import sqlite3
from flask import current_app, globals
from flask.cli import with_appcontext


def get_db():
    if 'db' not in globals:
        globals.db = sqlite3.connect(
            current_app.config['SQLALCHEMY_DATABASE_URI'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        globals.db.row_factory = sqlite3.Row

    return globals.db


def close_db(e=None):
    db = globals.pop('db', None)

    if db is not None:
        db.close()
