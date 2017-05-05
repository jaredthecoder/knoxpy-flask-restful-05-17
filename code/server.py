#!/usr/bin/env python3


# Import Flask, Flask-RESTful, Flask-HTTPAuth
from flask import Flask, jsonify, abort, make_response, Response, render_template
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth


# Make the Flask App Instance

# Initialize Flask-RESTful's API object

# Wrap the API in HTTPBasicAuth for minimum password-based security

# Write Python function for authenticating via password

# Write Python function for handling unauthorized users

# Some hard-coded tasks, essentially our "database"
tasks = [
    {
        'id': 1,
        'title': 'Go to KnoxPy',
        'description': 'Present on building REST APIs in Python',
        'done': True
    },
    {
        'id': 2,
        'title': 'Go to BSides Knoxville',
        'description': 'Learn about infosec!',
        'done': False
    },
    {
        'id': 3,
        'title': 'Present at BSides Knoxville',
        'description': 'Be at the KEC at 9 to talk about Cross-Site Scripting',
        'done': False
    },

    {
        'id': 4,
        'title': 'Present at Codestock',
        'description': 'Demo forensic analysis of a Windows machine infected by Stuxnet',
        'done': False
    },

]

# Define the fields for our tasks

# Define a Resource for the Task list view
# GET: Return the entire current task list
# POST: Add a new task to the list

# Define a Resource for individual tasks
# GET: Get a task by an ID
# PUT: Update a task's data by an ID
# DELETE: Delete a task by an ID


# Define a Resource for the homepage of the ToDo application

# Add our resources to our API


# Write our main function
