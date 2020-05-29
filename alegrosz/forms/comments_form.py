from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired


class NewCommentForm(FlaskForm):
    content = TextAreaField("Comment", validators=[DataRequired("Data is required")])
    item_id = HiddenField(validators=[DataRequired()])
    submit = SubmitField("Send comment")
