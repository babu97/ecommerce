from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
boostrap = Bootstrap()
bycrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    boostrap.init_app(app)
    db.init_app(app)
    bycrypt.init_app(app)
    login_manager.init_app(app)

    from .admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from .carts import carts as carts_blueprint

    app.register_blueprint(carts_blueprint, url_prefix="/carts")

    from .customers import customers as customers_blueprint

    app.register_blueprint(customers_blueprint, url_prefix="/customers")

    from .products import products as products_blueprint

    app.register_blueprint(products_blueprint, url_prefix="/products")

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
