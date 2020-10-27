from flaskr import db, create_app


def test_init():
    app = create_app()
    assert db.app is app
