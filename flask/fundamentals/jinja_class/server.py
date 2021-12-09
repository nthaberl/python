from flask import Flask, render_template
app = Flask (__name__)

my_friends = [
    "Jim",
    "Shawn",
    "Andrew",
    "Shalini",
    "Michael"
]

@app.route("/")
def index():
    return "This is the start of our very cool adventure"

@app.route("/person")
def person():
    return render_template("person.html", name="Natascha") #can render in phrases or times

@app.route("/person/<Gname>")
def var_person(Gname):
    return render_template("person.html", name = Gname, friends = my_friends)

if __name__ == "__main__":
    app.run(debug = True)