from flaskr import create_app, db
from pathlib import Path
import pytest


@pytest.fixture
def client():
    app = create_app()
    app.testing = True

    db.create_all()  # setup
    yield app.test_client()  # tests run here
    db.drop_all()  # teardown


def test_database(client):
    """initial test. ensure that the database exists"""
    tester = Path("test.db").is_file()
    assert tester
