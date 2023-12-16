#!/usr/bin/python3
"script that starts a Flask web application"
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_clone():
    "script that starts a Flask web application"
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "script that starts a Flask web application"
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    "script that starts a Flask web application"
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    "script that starts a Flask web application"
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    "script that starts a Flask web application"
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
