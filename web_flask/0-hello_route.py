#!/usr/bin/python3
"first flask ksnkdnskdsa"
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_clone():
    "blablabalblabalsvv ddffldlf slfdslf ldf "
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)