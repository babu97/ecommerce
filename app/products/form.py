from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileField, FileRequired


class nameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField("Add")


class Addproducts(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    discount = IntegerField("Discount", default=0)
    stock = IntegerField("stock", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    colors = TextAreaField("colors", validators=[DataRequired()])
    image_1 = FileField("image_1", validators=[FileRequired(), FileAllowed('jpg','png','gif','jpeg')],
                        'images only please')
