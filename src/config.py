from pathlib import Path
from flask import Flask

basedir = Path(__file__).parent


class Config(object):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'my-key'
    SQLALCHEMY_DATABASE_URI = 'postgres://yaxqouiimjpmtm:6617a1c5caa35b46e75a6172a44c51cad90d9d77b89f777e196194a13cc4' \
                              '52e5@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d6hf47p3m72qto'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/uni'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REST_URL_PREFIX = '/api'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
