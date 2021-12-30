import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    BPDTS_API_URL = 'https://bpdts-test-app.herokuapp.com'


class TestingConfig(Config):
    TESTING = True
    BPDTS_API_URL = 'mock'


class ProductionConfig(Config):
    BPDTS_API_URL = 'https://bpdts-test-app.herokuapp.com'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
