from app import db
from flask_login import UserMixin

# User class with one-to-many recipes relationship.
# The class inherits from UserMixin to implement critical flask-login functions automatically.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    recipes = db.relationship("Recipe")

# Recipe class that links back to the author (user).
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(32))
    ingredients = db.Column(db.String(32))
    instructions = db.Column(db.String(32))
    created = db.Column(db.DateTime(timezone=True))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))