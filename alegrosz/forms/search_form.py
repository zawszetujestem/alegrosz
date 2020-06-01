from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchItem(FlaskForm):
    search = StringField("What you are looking for", validators=[DataRequired("Data required. What you are looking for")])
    submit = SubmitField("Search")