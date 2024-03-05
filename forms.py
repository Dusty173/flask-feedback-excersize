"""Forms for feedback"""

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    """Form for logging in"""

    username = StringField("Username:", validators=[InputRequired(), Length(min = 2, max = 20)])
    password = PasswordField("Password:", validators=[InputRequired(), Length(min= 5, max=50)])

class RegisterForm(FlaskForm):
    """Register user form"""
    username = StringField("Username:", validators=[InputRequired(), Length(min = 2, max = 20)])
    password = PasswordField("Password:", validators=[InputRequired(), Length(min= 5, max=50)])
    email = StringField("Email:", validators=[InputRequired(), Length(max=50)])
    first_name = StringField("First name:", validators=[InputRequired(), Length(max=30)])
    last_name = StringField("Last name:", validators=[InputRequired(), Length(max=30)])

class FeedbackForm(FlaskForm):
    """Form for adding feedback"""
    title = StringField("Title:", validators=[InputRequired(), Length(max=30)])
    content = StringField("Add Content:", validators=[InputRequired(), Length(max=140)])

class DeleteForm(FlaskForm):
    """Leave empty so we can use this as a post route to delete things"""