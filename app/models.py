from datetime import datetime
from flask_login import UserMixin
from . import db, bycrypt, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=False)

    def __init__(
        self, email, password, is_admin=False, is_confirmed=False, confirmed_on=None
    ):
        self.email = email
        self.password = bycrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed_on = confirmed_on

    def __repr__(self):
        return f"<email{{self.email }}>"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))