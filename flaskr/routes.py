from flaskr import create_app

app = create_app(

)


@app.route('/hello')
def hello():
    return "Hello, gangster man!"
