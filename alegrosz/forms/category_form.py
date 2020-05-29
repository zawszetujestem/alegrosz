from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField

from alegrosz.forms.item_form import NewItemForm
from alegrosz.utils.validators.belongs_to_other_field_option import BelongsToOtherFieldOption


class CategoryForm(NewItemForm):
    category = SelectField("Category", coerce=int)
    subcategory = SelectField("Subcategory", coerce=int,
                              validators=[BelongsToOtherFieldOption(table='subcategories', belongs_to="category", message='Select different category ')])
    submit = SubmitField("Submmit")
