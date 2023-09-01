from datetime import datetime
from flask_login import UserMixin
from flask import current_app
from . import db, bycrypt, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


from itsdangerous import URLSafeSerializer


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, default=False)

    def __init__(
        self,
        email,
        username,
        password,
        is_admin=False,
        is_confirmed=False,
        confirmed=False,
    ):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed = confirmed

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = URLSafeSerializer(current_app.config["SECRET_KEY", expiration])
        return s.dumps(
            {"confirm": self.id}, salt=current_app.config["SECURITY_PASSWORD_SALT"]
        )

    def confirm(self, token):
        s = URLSafeSerializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token, salt=current_app.config["SECURITY_PASSWORD_SALT"])
        except:
            return False
        if data.get("confirm") != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return f"<email{{self.email }}>"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
