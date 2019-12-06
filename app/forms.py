import wtforms as wtf
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = wtf.StringField('Username', validators=[DataRequired()])
    password = wtf.PasswordField('Password', validators=[DataRequired()])
    remember_me = wtf.BooleanField('Remember me')
    submit = wtf.SubmitField('Sign In')
