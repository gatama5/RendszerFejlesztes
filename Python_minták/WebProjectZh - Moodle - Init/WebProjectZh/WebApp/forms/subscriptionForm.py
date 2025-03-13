from flask_wtf import FlaskForm
from sqlalchemy.orm import Mapped
from wtforms import BooleanField, StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length, NoneOf, AnyOf


class SubscriptionForm(FlaskForm):

### Write your solution here!
    coursecode = StringField('Course Code', validators = [DataRequired()])
    neptun = StringField('Neptun', validators = [DataRequired(),Length(6)])
    name = StringField('Name', validators = [DataRequired()])
    iamhuman = BooleanField('I am human!',validators= [DataRequired()] )
    submit = SubmitField('Subscription')
###    
