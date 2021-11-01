from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    print(request.form)
    session['name'] = request.form ['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['vehicle'] = request.form.get('vehicle')
    session['comment'] = request.form['comment']

    return redirect("/result")

@app.route("/result")
def result():
    print(request.form)
    return render_template ("result.html", name = session['name'], location = session['location'], language = session['language'], vehicle = session['vehicle'], comment = session['comment'])

if __name__ == "__main__":
    app.run(debug = True)