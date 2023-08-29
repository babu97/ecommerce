from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from .carts import carts as carts_blueprint

    app.register_blueprint(carts_blueprint, url_prefix="/carts")

    from .customers import customers as customers_blueprint

    app.register_blueprint(customers_blueprint, url_prefix="/customers")

    from .products import products as products_blueprint

    app.register_blueprint(products_blueprint, url_prefix="/products")

    from .shop import shop as shop_blueprint

    app.register_blueprint(shop_blueprint)

    return app
