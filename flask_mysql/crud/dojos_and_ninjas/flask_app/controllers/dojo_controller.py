from flask import render_template, redirect, request
from flask_app import app #inside flask app, dunder init app
from flask_app.models.dojo import Dojo #inside flask_app, into models, into user file, bringing in User class



@app.route("/")
def index():
    return redirect("/dojos")

#READ MANY
@app.route("/dojos")
def get_all():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojos.html", all_dojos = all_dojos)

#CREATE - RENDER
@app.route("/dojos/new")
def new_dojo_form():
    return render_template("create.html")

#CREATE - POST ROUTE
@app.route("/dojos/create", methods = ["POST"])
def create_new_dojos():
    print(request.form)
    Dojo.create(request.form)
    
    return redirect("/dojos")


#READ ONE
@app.route("/dojos/<int:dojo_id>")
def display_dojo(dojo_id):
    return render_template("single_dojo.html", dojo = Dojo.read_one({ 'id': dojo_id }))

#UPDATE - RENDER
@app.route("/dojos/<int:dojo_id>/edit")
def update_form(dojo_id):
    return render_template("edit_dojo.html", dojo = Dojo.read_one({ 'id': dojo_id }))

#UPDATE - POST ROUTE
@app.route("/dojos/<int:dojo_id>/update", methods = ["POST"])
def update_dojo(dojo_id):
    print(request.form)
    data = {
        **request.form, #copies over all the data from the request.form dictionary
        "id": dojo_id
    }
    Dojo.update(data)
    return redirect(f"/dojos/{dojo_id}")

#DELETE
@app.route("/dojos/<int:dojo_id>/destroy")
def delete_dojo(dojo_id):
    Dojo.delete({'id': dojo_id})

    return redirect("/dojos")