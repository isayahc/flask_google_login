from flaskr import create_app, db

app = create_app(

)


@app.route('/hello')
def hello():
    return "Hello, gangster man!"

# @app.route('/africa')
# def hello():
    
#     return "Hello, gangster man!"
