from flask import current_app as app
from . import db
from .models import User


@app.route('/hello')
def hello():
    return "Hello, gangster man!"
