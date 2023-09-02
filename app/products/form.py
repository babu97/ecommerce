from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class nameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField("Add")
