from app import myapp_obj
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from app import db
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime

### UNAUTHENTICATED ROUTES ###
@myapp_obj.route("/")
@myapp_obj.route("/recipes")
def view_all_recipes():
    # For each recipe, we will get the title and store it in the recipes list
    recipes = []
    for recipe in Recipe.query.all():
        recipes.append((recipe.title, User.query.get(recipe.author).username, recipe.id))
    
    # We will pass the recipes list to the template to allow it to create the recipes page
    return render_template("all_recipes.html", recipes=recipes)

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user's password

        # Fetch a user by that username
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            # Check that the passwords match
            if form.password.data == user.password:
                # Login the user, and remember the session if the box is checked
                login_user(user, remember=form.remember_me.data)

                flash('Logged in successfully.')

                next = request.args.get('next')

                return redirect(next or url_for('view_all_recipes'))
        
        flash('Login details were incorrect.')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@myapp_obj.route("/logout")
@login_required
def logout():
    # Logout the user and bring them to the homepage
    logout_user()
    return redirect(url_for('view_all_recipes'))

### AUTHENTICATED ROUTES ###
@myapp_obj.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        r = Recipe(title=form.title.data,
                   description=form.description.data,
                   ingredients=form.ingredients.data,
                   instructions=form.instructions.data,
                   created=datetime.now(),
                   author=current_user.id) # Associate the recipe with the logged in user (one-to-many)
        # Save this recipe to the database
        db.session.add(r)
        db.session.commit()
        # Redirect to the recipe's details
        return redirect(f"/recipe/{r.id}")
    return render_template('create_recipe.html', form=form)

@myapp_obj.route("/recipe/<integer>")
@login_required
def view_single_recipe(integer):
    recipe = Recipe.query.get(integer)
    user = User.query.get(recipe.author)
    return render_template('view_recipe.html', recipe=recipe, user=user)

@myapp_obj.route("/recipe/<integer>/delete")
@login_required
def delete_recipe(integer):
    recipe = Recipe.query.get(integer)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('view_all_recipes'))