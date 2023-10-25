#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print Web """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print Web """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """  display “C ” followed by the value of the text variable """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is_cool"):
    """ display text """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ number route """
    return "{:d} is a number".format(n)
@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """ number template """
    return render_template("5-number.html", n=n)
if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
