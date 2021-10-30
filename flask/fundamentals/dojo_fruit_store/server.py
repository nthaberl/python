from datetime import datetime

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "keep it secret, keep it safe."

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # print(request.form)
    session['strawberry_count'] = request.form ['strawberry']
    session['raspberry_count'] = request.form['raspberry']
    session['apple_count'] = request.form ['apple']
    session['first_name'] = request.form ['first_name']
    session['last_name'] = request.form ['last_name']
    session['student_id'] = request.form ['student_id']
    session['count'] = int(session['strawberry_count']) + int(session['raspberry_count']) + int(session['apple_count'])
    session['date'] = datetime.now()
    print ("Charging ",(session['first_name'])," for", (session['count']), "fruits")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template('fruits.html')

if __name__=="__main__":   
    app.run(debug=True)