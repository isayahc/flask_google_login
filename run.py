from flaskr import create_app
import gunicorn

app = create_app()

if __name__ == '__main__':
    # app.server = server
    server = app.server
    app.run(debug=False)
