from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import Length


class FilterForm(FlaskForm):
    title = StringField("Title", validators=[Length(max=20)])
    adv_filter = BooleanField("Advance filtering")
    price = SelectField("Price", coerce=int, choices=[(0, '---'), (1, "max to min"), (2, "min to max")])
    category = SelectField("Category", coerce=int)
    subcategory = SelectField("Subcategory", coerce=int)
    submit = SubmitField("Filter")