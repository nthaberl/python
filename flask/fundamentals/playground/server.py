from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome to the playground!"

@app.route('/play/<int:num>/<string:color>')
def playground(num, color):
    return render_template("index.html", times=num, color=color)

if __name__=="__main__":
    app.run(debug=True) 