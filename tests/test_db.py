from flaskr import db, create_app
from flaskr.models import User
import pytest
import os


def test_init():
    app = create_app()
    assert db.app is app


def test_get_user():
    app = create_app()
    app.config['TESTING'] = True
    app.app_context().push()
    user = User.get(1)
    assert user is not None

from flaskr import create_app
import tempfile

@pytest.fixture
def client():
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
