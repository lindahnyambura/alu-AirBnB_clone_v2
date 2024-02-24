#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ def doc: return C with text """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ def doc: return python with text or default text """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    def doc: return number if int else return not a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)