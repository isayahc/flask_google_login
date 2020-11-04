from flaskr import create_app
import gunicorn

app = create_app()
server = app.server

if __name__ == '__main__':
    app.run(debug=False)
