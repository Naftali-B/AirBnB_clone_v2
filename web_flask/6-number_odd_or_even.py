#!/usr/bin/python3

''' starts a Flask web app '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ / displays 'Hello HBNB' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ /hbnb displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ displays C followed by value of text passed """
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ displays Python followed by value of text """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def check_integer(n):
    """ Displays 'n is a number' only if n is an integer """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_number_template(n):
    """ Displays an HTML page only if n is an integer """
    return render_template('number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    ''' displays HTML page only if n is an integer '''
    if n % 2 == 0:
        myint = 'even'
    else:
        myint = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, myint=myint


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
naf@Naftali:~/AirBnB_clone_v2/web_flask$
naf@Naftali:~/AirBnB_clone_v2/web_flask$
