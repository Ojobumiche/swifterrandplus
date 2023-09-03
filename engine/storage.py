#!/usr/bin/python3
''' Defines the file storage class '''

import json
from models.base_model import BaseModel
from base_model import Users
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""Create Flask application instance and 
store it in the app variable
"""
app = Flask(__name__)
"""mysql databaseURL"""
"""MySQL database URL"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/swifterrandplus'

db = SQLAlchemy['SQLAlchemy_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""Create User Data Model.
User model represent the user_data table"""


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.String(15), nullable=False)
