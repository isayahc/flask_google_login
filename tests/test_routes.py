from flaskr import routes


def test_index():
    x = routes.hello()
    assert x == 'Hello, gangster man!'
