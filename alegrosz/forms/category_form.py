from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

from alegrosz.forms.item_form import NewItemForm


class CategoryForm(NewItemForm):
    category = SelectField("Category", coerce=int)
    subcategory = SelectField("Subcategory", coerce=int)
    submit = SubmitField("Submmit")
