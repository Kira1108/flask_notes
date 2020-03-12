from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
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


@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me = {}".format(
        form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title = 'Sign in', form = form)
