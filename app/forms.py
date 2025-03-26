from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    submit = SubmitField("Login")
    remember_me = BooleanField("Remember Me")

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[validators.DataRequired()])
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    submit = SubmitField("Sign Up")

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[validators.DataRequired(), validators.Length(max=80)])
    description = TextAreaField('Description', validators=[validators.DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[validators.DataRequired()])
    instructions = TextAreaField('Instructions', validators=[validators.DataRequired()])
    submit = SubmitField("Submit Recipe")
