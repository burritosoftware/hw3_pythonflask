from app import myapp_obj
from flask import render_template
from flask import redirect
from app.forms import LoginForm
from app.models import User
from app import db
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    name = "carlos"
    return render_template("hello.html", name=name)

@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)
    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))
