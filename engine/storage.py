#!/usr/bin/python3
"""Import SQLALCHEMY library"""
import os
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Create the SQLite database engine
engine = create_engine("sqlite:///user.db")

# Create a base class for declarative models
Base = declarative_base()

# Define the User model


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(25), nullable=False)  # Fixed typo here
    phone_number = Column(Integer, nullable=False)  # Fixed typo here
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"user_id: {self.user_id}, username: {self.username}, email: {self.email}, password: {self.password}, phone_number: {self.phone_number}, created_at: {self.created_at}"


# Create the table in the database
Base.metadata.create_all(engine)
