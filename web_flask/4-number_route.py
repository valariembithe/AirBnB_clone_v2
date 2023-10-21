from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print Web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print Web """
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    """  display “C ” followed by the value of the text variable """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="is_cool"):
    """ display text """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<n>')
def number(n):
    if n is type(int):
        return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
