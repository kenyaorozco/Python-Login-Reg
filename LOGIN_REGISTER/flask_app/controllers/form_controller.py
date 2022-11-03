print("controller file running")

from flask import render_template,redirect,request,session, Flask,flash
from flask_app import app
from flask_app.models.login import Login
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 


@app.route("/")
def main_page():
    return render_template("form.html")


@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/login",methods=["post"])
def login_page():
    data = {"email": request.form["email"]}
    user_in_db = Login.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect("/")

    session['user_id'] = user_in_db.id
    # if not Login.validate_login(data):
    return 'you are logged in'
    # return 'hey ur in '

@app.route("/register/submit",methods=["post"])
def registration():

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password": pw_hash,
    }
    if not Login.validate_user(data):
        return redirect("/register")

    new_user = Login.save(data)
    session["new_user"] = new_user
    print(f"new user is {new_user}")
    return redirect ("/")

@app.route("/home")
def send_home():
    return redirect("/")