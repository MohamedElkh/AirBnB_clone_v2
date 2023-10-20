#!/usr/bin/python3
""" start app listen on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def func_hello_hbnb():
    """ func to display hello"""
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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
