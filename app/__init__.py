from flask import Flask
from config import config
from flasgger import Swagger

swagger = Swagger()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    swagger.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')

    return app
