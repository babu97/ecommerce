from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from app.models import User
from app.utils import is_valid


class RegistationForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(1, 64)])
    username = StringField("username", validators=[DataRequired(), Length(1, 64)])
    email = StringField("Email Address", validators=[Email(), Length(1, 64)])
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            EqualTo("password1", message="passwords must match ."),
        ],
    )
    password1 = PasswordField(
        "confirm password",
        validators=[DataRequired(), EqualTo("password", message="password must match")],
    )
    submit = SubmitField("SignUp")

    def validate_email(self, field):
        if not is_valid(email=field.data.lower()):
            raise ValidationError("Email is invalid")
        user = User.query.filter_by(email=field.data.lower()).first()
        if user:
            raise ValidationError("Email already registered")

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data.lower()).first()
        if user:
            raise ValidationError("Username already Registered")


class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[Email(), Length(1, 64)])
    password = PasswordField("password", validators=[DataRequired()])

    submit = SubmitField("LogIn")
