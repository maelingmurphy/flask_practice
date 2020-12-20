from flask import Flask

app = Flask(__name__) # Create Flask application with the name app with name of current Python module

@app.route('/') # Decorator that turns a regular Python function into a Flask view function
def index():
    return "Welcome! This is the index page."

@app.route("/hi/")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"