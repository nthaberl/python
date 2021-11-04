from flask import Flask, render_template, redirect, request

from user import User #from file import class

app = Flask (__name__)
app.secret_key = "jingle jangle"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def read_all():
    all_users = User.get_all()
    print(all_users)
    return render_template("users.html", all_users = all_users)

@app.route("/users/create")
def new_user_form():
    return render_template("create.html")

@app.route("/users/new", methods = ["POST"])
def create_new_users():
    User.create(request.form)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug = True)