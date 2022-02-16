import os
basedir = os.path.abspath(os.path.dirname(__file__))
import urllib.request as req

password = "" 

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'abcde12345'
    SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_DATABASE_URL']
    SQLALCHEMY_BINDS = {
        'mysql':f"mysql+pymysql://root:{password}@localhost/mysql"
    }

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
