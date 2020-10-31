from flask import current_app as app
from . import db


@app.route('/hello')
def hello():
    return "Hello, gangster man!"

