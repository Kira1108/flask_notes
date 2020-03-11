from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"


@app.route('/test')
def test_user():
    user = {'username':'Huan'}
    posts = [
        {
            "author":{"username":"Huan"},
            "body":"Hi this is my first post."
        },
        {
            "author":{"username":"Duan"},
            "body":"I love your first post."
        },
        {
            "author":{"username":"Suan"},
            "body":"So do I."
        },

    ]

    return render_template('index.html',title = 'Home',user = user,posts = posts)
