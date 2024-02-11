#!/usr/bin/python3
"script that starts a Flask web application"
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    mod_text = "".join([" " if letter == "_" else letter for letter in text])
    return f"C {mod_text}"


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    mod_text = "".join([" " if letter == "_" else letter for letter in text])
    return f"Python {mod_text}"


@app.route("/number/<int:n>")
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route("/states_list")
def states_list():
    obj_list = storage.all("State")
    return render_template("7-states_list.html", obj_list=obj_list)

if __name__ == "__main__":
    """run forest dump"""
    app.run(debug=True, host="0.0.0.0", port=5000)
