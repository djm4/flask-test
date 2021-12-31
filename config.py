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

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class DockerConfig(Config):
    BPDTS_API_URL = 'https://bpdts-test-app.herokuapp.com'

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'docker': DockerConfig
}
