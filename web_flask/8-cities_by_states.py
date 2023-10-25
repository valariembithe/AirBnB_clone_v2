#!/usr/bin/python3
""" script that starts a Flask web application"""
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
    states = Storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
