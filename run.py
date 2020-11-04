from flaskr import create_app
import gunicorn

app = create_app()

if __name__ == '__main__':
    server = app.server
    app.run(debug=False)
