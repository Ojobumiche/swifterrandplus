#!/usr/bin/python3
"""Import SQLALCHEMY library"""
import os
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
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

"""Create a session to interact with the database"""
session = sessionmaker(bind=engine)
session = session()
# Define a function to create a new user login session


def create_user_session(username, password):
    try:
        # Check if the provided username and password match a user in the database
        user = session.query(User).filter_by(
            username=username, password=password).first()

        if user:
            # Session is created for the user
            print(f"User '{username}' logged in successfully!")
            return user
        else:
            print("Invalid username or password. Login failed.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


# Usage example
if __name__ == "__main__":
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Call the function to create a user session
    user_session = create_user_session(username_input, password_input)
    for user in user_session:
        print(user)
