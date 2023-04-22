#!/usr/bin/env python

"""
This script runs a simple web app on your localhost, port 5000, using the Flask library.

Routes:
    - '/': Returns the "main page" of the app.
    - '/json': Returns all the data from https://jsonplaceholder.typicode.com/todos.
    - '/json/user/<user_id>': Returns the data of a specific user ID. If the user ID does not exist, it returns an error message.
    Additionally, it has an error page that handles 404 errors.
    
Functions:
    - hello(): Returns the "main page" of the app.
    - get_json(): Returns all the data from https://jsonplaceholder.typicode.com/todos.
    - get_user_data(user_id: int): Returns the data of a specific user ID. If the user ID does not exist, it returns an error message.
    - page_not_found(e): Handles 404 errors and returns an error message.
"""

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# map "/" route to hello function
@app.route('/')
def hello():
    """
    This funstion return the "main page" of the app, for no spcific routing
    :return: string message
    """
    return 'Hi there!'


# map "/json" route to get_json function
@app.route('/json')
def get_json():
    """
    Returns all the data from https://jsonplaceholder.typicode.com/todos.
    :return: JSON-formatted data as the response body.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return jsonify(response.json())


# map "/json/user/<user_id>" route to get_user_data function
@app.route('/json/user/<user_id>')
def get_user_data(user_id: int):
    """
    Returns all the data of a specific user ID. If the user ID does not exist, it returns an error message.
    :param user_id: the user ID number of the user whose data you want to receive.
    :return: JSON-formatted data containing the data of a specified user ID, or an error message if the user ID does not exist.
    """
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    # check if the response is empty
    if len(response.json()) == 0:
        return f"No data found for user ID {user_id}."
    return jsonify(response.json())

@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors and returns an error message.
    :param e: the error that occurred.
    :return: a string message and a status code of 404.
    """
    return "Oops! That page doesn't exist.", 404

if __name__ == '__main__':
    app.run()