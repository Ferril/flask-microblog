import wtforms as wtf
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from flask_wtf import FlaskForm
from app.models import User


class LoginForm(FlaskForm):
    username = wtf.StringField('Username', validators=[DataRequired()])
    password = wtf.PasswordField('Password', validators=[DataRequired()])
    remember_me = wtf.BooleanField('Remember me')
    submit = wtf.SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = wtf.StringField('Username', validators=[DataRequired()])
    email = wtf.StringField('Email', validators=[DataRequired(), Email()])
    password = wtf.PasswordField('Password', validators=[DataRequired()])
    password2 = wtf.PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')],
    )
    submit = wtf.SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')
