from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired


class OrderForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    quantity = StringField("Quantity", validators=[DataRequired()])
    submit = SubmitField("Send order")


