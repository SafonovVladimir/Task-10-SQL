from pathlib import Path

# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = Path(__file__).parent


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'my-key'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/uni'
    # DATABASE_URL = 'postgresql://admin:admin@localhost/uni'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
