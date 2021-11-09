from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja

@app.route("/ninjas")
def new_ninja():
    return render_template("/ninjas/new_ninja.html", all_dojos = Dojo.get_all())



@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    print(request.form)
    Ninja.create(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f"/dojos/{dojo_id}") #routes back to dojo where ninja was created
    # return redirect ("/dojos")


# @app.route("/users/create") #going forward, call this /new
# def new_user_form():
#     return render_template("create.html")

# #UPDATE - RENDER
# @app.route("/ninjas/<int:ninja_id>/edit")
# def update_ninja_form(ninja_id):
#     return render_template("edit_ninja.html", ninja = Ninja.read_one_ninja({ 'id': ninja_id }))

# #UPDATE - POST ROUTE
# @app.route("/ninjas/<int:ninja_id>/update", methods = ["POST"])
# def update_ninja(ninja_id):
#     print(request.form)
#     data = {
#         **request.form, #copies over all the data from the request.form dictionary
#         "id": ninja_id
#     }
#     Ninja.update(data)
#     return redirect(f"/ninjas/{ninja_id}")


# #DELETE
# @app.route("/ninjas/<int:ninja_id>/destroy")
# def delete_ninja(ninja_id):
#     Ninja.delete({'id': ninja_id})
#     return redirect("/dojos")
