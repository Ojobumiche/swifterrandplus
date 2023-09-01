#
#!/usr/bin/python3
"""Defines the User class."""

from base_model import BaseModel

class User(BaseModel):
    """Represents a User.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, username, email, password, first_name, last_name):
        super().__init__()  # Call the constructor of the base class
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def register(cls):
        username = input("Enter username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        return cls(username, email, password, first_name, last_name)

    @staticmethod
    def login(users):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        username = input("Enter your username: ")

        for user in users:
            if user.email == email and user.password == password and user.username == username:
                print("Login successful!")
                return
        print("Invalid email, username, or password.")

if __name__ == "__main__":
    """ Register a new user"""
    new_user = User.register()

    """ Store user objects in a list (simulating a database)"""
    users_list = [new_user]

    """ User login"""
    User.login(users_list)

