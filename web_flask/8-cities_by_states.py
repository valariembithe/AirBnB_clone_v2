#!/usr/bin/python3
""" script that starts a Flask web application
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def close_db(exc):
    """ remove the current SQLAlchemy Session """
    storage.close()

@app.route('/cities_by_states')
def states_list():
    """ a states list """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    storage.reload()
    app.run(host='0.0.0.0', port=5000)

