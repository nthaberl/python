from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 0 # setting session data
    # print(session['count'])
    return render_template("index.html")

@app.route('/add_session')
def add_session():
    session['count'] = session['count'] + 1
    return redirect ('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/input', methods = ["POST"])
def user():
    session['count'] += int(request.form['input']) - 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

