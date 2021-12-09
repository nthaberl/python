from flask import Flask, render_template  # Import Flask to allow us to create our app, will need this in every app we build

app = Flask(__name__)    # Create a new instance of the Flask class called "app", will need this in every app built with flask

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
        # Instead of returning a string, 
        # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template("index.html", phrase="hello", times=5)

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return 'success'


@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name', always defaults to a string
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35}, #this whole dictionary is a row
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


@app.route('/goodbye/<string:banana>/<int:num>')
def goodbye(banana, num):
    return f"Hello {banana * num}"

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
# app.run(debug=True) should be the very last statement! 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.