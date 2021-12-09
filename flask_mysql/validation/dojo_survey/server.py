from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    print(request.form)
    # session['vehicle'] = []
    # if request.form['vehicle']:
    #     session['vehicle'].append(request.form['vehicle'])
    # else:
    #     session['vehicle'] = request.form['vehicle']
    # if request.form.getlist('vehicle1') == True:
    #     session['vehicle'].append(request.form['vehicle1'])
    # if request.form.getlist('vehicle2') == True:
    #     session['vehicle'].append(request.form['vehicle2'])
    # if request.form.getlist('vehicle3') == True:
    #     session['vehicle'].append(request.form['vehicle3'])
    session['name'] = request.form ['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['vehicle'] = request.form.getlist('vehicle')
    session['comment'] = request.form['comment']
    print(session['vehicle'])
    return redirect("/result")

@app.route("/result")
def result():
    print(request.form)
    return render_template ("result.html", name = session['name'], location = session['location'], language = session['language'], vehicle = session['vehicle'], comment = session['comment'])

if __name__ == "__main__":
    app.run(debug = True)