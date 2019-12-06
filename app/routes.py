from flask import render_template
from app import app
from .forms import LoginForm

# this is view with url paths '/' and '/index'
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ferril'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
