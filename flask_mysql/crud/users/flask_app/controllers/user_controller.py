from flask import render_template, redirect, request
from flask_app import app #inside flask app, dunder init app
from flask_app.models.user import User #inside flask_app, into models, into user file, bringing in User class

@app.route("/")
def index():
    return render_template("index.html")

#READ MANY
@app.route("/users")
def read_all():
    all_users = User.get_all()
    print(all_users)
    return render_template("users.html", all_users = all_users)

#CREATE - RENDER
@app.route("/users/create")
def new_user_form():
    return render_template("create.html")

#CREATE - POST ROUTE
@app.route("/users/new", methods = ["POST"])
def create_new_users():
    print(request.form)
    User.create(request.form)
    
    return redirect("/users")


#READ ONE
@app.route("/users/<int:user_id>")
def display_user(user_id):
    return render_template("one_user.html", user = User.read_one({ 'id': user_id }))

#UPDATE - RENDER
@app.route("/users/<int:user_id>/edit")
def update_form(user_id):
    return render_template("edit_user.html", user = User.read_one({ 'id': user_id }))

#UPDATE - POST ROUTE
@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    print(request.form)
    data = {
        **request.form, #copies over all the data from the request.form dictionary
        "id": user_id
    }
    User.update(data)
    return redirect(f"/users/{user_id}")


#DELETE
@app.route("/users/<int:user_id>/destroy")
def delete_user(user_id):
    User.delete({'id': user_id})

    return redirect("/users")