from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DicePostForm(FlaskForm):
    link = StringField('Burn', validators=[DataRequired()])
    submit = SubmitField('Post')