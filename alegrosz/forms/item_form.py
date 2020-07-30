from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField, DecimalField
from wtforms.validators import DataRequired, InputRequired, Length

from alegrosz.forms.price_field import PriceField


class NewItemForm(FlaskForm):
    title = StringField("Title",
                        validators=[InputRequired("Input is required"),
                                    DataRequired("Data is required"),
                                    Length(min=5, max=20, message="Input must be between 5 and 20 characters")])
    description = TextAreaField("Description",
                                validators=[InputRequired("Input is required"),
                                            DataRequired("Data is required"),
                                            Length(min=5, max=40, message="Input must be between 5 and 40 characters")])
    price = PriceField("Price", validators=[DataRequired("Data is required")])
    image = FileField('Image', validators=[FileAllowed(["jpg", "jpeg", "png"], "Images only")])


class EditItemForm(NewItemForm):
    submit = SubmitField("Update item")


class RemoveItemForm(FlaskForm):
    submit = SubmitField("Remove item")

