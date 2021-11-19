
from flask import render_template, redirect, request, jsonify, make_response

from flask_app import app
from flask_app.models.trail import Trail


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/trails")
def get_all_trails():
    return jsonify(Trail.get_all())

@app.route("/api/trails/create", methods = ["POST"])
def create_trail():
    print(request.json)
    Trail.create(request.json)
    return jsonify