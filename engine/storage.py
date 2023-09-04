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
    password = db.column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(20))
    created_at = db.column(db.DateTime, default=db.func.now())
    tasks = db.relationship('Task', backref='user', lazy=True)


class Agent(db.Model):
    agent_id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100), nullable=False)
    email = db.column(db.String(100), unique=True, nullable=False)
    phone_number = db.column(db.String(20))
    availability = db.column(db.Boolean, default=True)
    created_at = db.Column(db.DataTime, default=db.func.now())

    """one-to-many relationship with task"""
    tasks = db.relationship('Task', backref='agent', lazy=True)

    """Define the Task model to establish the relationships"""


class Task(db.Model):
    task_id = db.Column(db.Integer, Primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    # you can define other status options
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=db.func.now())

    """Foreign keys to connect User and Agent"""
    user_id = db.Column(db.Integer, db.ForeignKey
                        ('user.user_id'), nullable=False)

    agent_id = db.Column(db.Integer, db.ForeignKey
                         ('agent.agent_id'))

    """Create the database table"""
    with app.app_context():
        db.create_all()
