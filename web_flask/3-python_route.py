#!/usr/bin/python3
""" start flask web app """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def func_hello_hbnb():
    """ func to display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def func_hbnb():
    """ func to display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def func_c(text):
    """func to display c and value text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def func_python(text="is cool"):
    """ func to display python with value text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
