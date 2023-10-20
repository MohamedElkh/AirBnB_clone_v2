#!/usr/bin/python3
"""start flask app on port 5000"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def func_hello_hbnb():
    """func to display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def func_hbnb():
    """func to display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def func_c(text):
    """func to display c with value text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def func_python(text="is cool"):
    """func to display python and value text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def func_number(n):
    """ func to display n is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def func_number_template(n):
    """func to display html page"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
