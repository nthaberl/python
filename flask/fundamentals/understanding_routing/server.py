from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<string:phrase>")
def repeat(num, phrase):
    return f"{phrase * num}"

@app.route("/<string:bananas>")
def wrong(bananas):
    return "Sorry! No response!!"

if __name__=="__main__":
    app.run(debug=True) 