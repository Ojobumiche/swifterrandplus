#!/usr/bin/python3
''' Defines the file storage class '''

import json
from models.base_model import BaseModel
from base_model import Users
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
"""mysql databaseURL"""
app.config['SQLAlchemy_DATABASE_URL']= 'mysql:///swifterrandplus.db'
db = SQLAlchemy['SQLAlchemy_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
"""Create User Data Model.
User model represent the user_data table"""

class UserData(db.Model):
    id = db.Column(db.integer,
    primary_key= True)
    email = db.Column(db.String(120),
    unique=True, nullable=False)
    tel = db.Column(db.String(15),
    nullable=False) 
    
    

