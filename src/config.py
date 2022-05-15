from pathlib import Path
from flask import Flask

basedir = Path(__file__).parent


class Config(object):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'my-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/uni'
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
