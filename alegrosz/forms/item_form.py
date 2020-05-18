from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class NewItemForm(FlaskForm):
    title = StringField("Title")
    description = TextAreaField("Description")
    price = StringField("Price")
    submit = SubmitField()

