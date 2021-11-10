from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.user import User #import both models!
from flask_app.models.recipe import Recipe


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect ("/") #redirects user back to homepage if not logged in
    return render_template ("dashboard.html", user = User.get_by_id ({ "id": session["user"]}), all_recipes = Recipe.get_all())

##CREATE

@app.route("/recipes/new")
def new_recipe():
    return render_template("new_recipe.html")


@app.route("/recipes/create", methods = ["POST"])
def create_recipe():
    if not Recipe.validate(request.form):
        return redirect("/recipes/new")

    #dictionary has to be created because no user_id is being input into the form
    data = {
        **request.form,
        "user_id": session["user"]
    }

    Recipe.create(data)

    return redirect("/dashboard")

##READ
@app.route("/recipes/<int:id>")
def display_recipe(id):
    return render_template("recipe.html", user = User.get_by_id ({ "id": session["user"]}), recipe = Recipe.get_one({"id": id}))

##UPDATE
@app.route("/recipes/<int:id>/edit")
def edit_recipe(id):
    return render_template("edit_recipe.html", recipe = Recipe.get_one({"id": id}), user = User.get_by_id ({ "id": session["user"]})) ##prepopulating fields with info from object

@app.route ("/recipes/<int:id>/update", methods = ["POST"])
def update_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f"/recipes/{id}/edit")
    #need to create dictionary because user is not updating the request form, so can not just send request form to update method
    data = {
        **request.form,
        "id": id
    }

    Recipe.update(data)

    return redirect("/dashboard")

#DELETE
@app.route ("/recipes/<int:id>/delete")
def delete_recipe(id):
    Recipe.delete({"id": id})

    return redirect ("/dashboard")
