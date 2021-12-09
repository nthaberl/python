from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form_submit", methods = ["POST"])
def form_submit():
    print(request.form)

    session["ccn"] = request.form["ccn"]
    session["ssn"] = request.form["ssn"]
    session["flower"] = request.form["flower"]

    return redirect("/new")


@app.route("/new")
def new_route():
    print(request.form)
    return render_template(
        "new.html", 
        ccn = session["ccn"], 
        ssn = session["ssn"], 
        flower = session["flower"]
    )


if __name__ == "__main__":
    app.run(debug = True)