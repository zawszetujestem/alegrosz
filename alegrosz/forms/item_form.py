from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField, DecimalField
from wtforms.validators import DataRequired

from alegrosz.forms.price_field import PriceField


class NewItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    price = PriceField("Price")
    image = FileField("Image", validators=[FileAllowed(["jpg", "jpeg", "png"], "Images only")])


class EditItemForm(NewItemForm):
    submit = SubmitField("Update item")


class RemoveItemForm(FlaskForm):
    submit = SubmitField("Remove item")

