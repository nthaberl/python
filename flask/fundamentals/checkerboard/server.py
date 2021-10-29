from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/<int:num1>/<int:num2>')
def check(num1, num2):
    return render_template("index.html", num1 = num1, num2 = num2)

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def colors(num1,num2,color1,color2):
    return render_template("index.html", num1 = num1, num2 = num2, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True) 