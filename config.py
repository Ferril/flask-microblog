import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG') or True
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
