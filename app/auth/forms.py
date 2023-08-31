from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


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


class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[Email(), Length(1, 64)])
    password = PasswordField("password", validators=[DataRequired()])

    submit = SubmitField("LogIn")
