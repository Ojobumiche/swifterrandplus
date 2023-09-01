#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User.

    Attributes:
        email (str): The email address of user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    def __init__(self,username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        
    """user registration"""
    def register():
        username = input("Enter username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        return User(username, email, password, first_name, last_name)
    
        """User login"""
    def login(users):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        username = input("Enter your username: ")
    
        for user in users:
            if user.email == email and user.password == password:
                print("Login successful!")
            else:
                 print("Invalid email or password.")
    
    """Register a new user"""
    new_user = register()
    
    """Store user objects in a list (simulating a database)
    """
    users_list = [new_user]
    
    """User login"""
    login(users_list)

    
    
    
    
user1 = User('email', 'password', 'username', 'first_name', 'last_name' )
user1.register()
print(user1.register)
