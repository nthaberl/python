from flask import render_template, redirect, request, session

from flask_bcrypt import Bcrypt #imports bcrypt class

from flask_app import app

from flask_app.models.user import User

bcrypt = Bcrypt(app) #lets us utilize bcrypt


#CAN ORGANIZE VIA DISPLAY/ACTION ROUTES OR C.R.U.D.

@app.route("/")
def index():
    if "user" in session:
        return redirect ("/dashboard") #if user already logged in no need to make user login again
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
    if not User.register_validator(request.form):
        return redirect ("/")

    hashpass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password": hashpass
    }

    user_id = User.create(data)
    #unique user ID
    session["user"] = user_id #user_id is a variable that was made above that is stored into session!

    return redirect("/dashboard")

@app.route("/login", methods = ["POST"])
def login():
    if not User.login_validator(request.form):
        return redirect ("/")

    user = User.get_by_email({"email": request.form["email"]})

    session["user"] = user.id #user holds User OBJECT and we need to access the id here

    return redirect ("/dashboard")


@app.route("/logout")
def logout():
    session.clear()

    return redirect ("/")

