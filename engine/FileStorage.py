import json
import os

class FileStorage:
    """Represent a storage engine for user logins.

    Attributes:
        __file_path (str): The path to the file where user login information is stored.
        __logins (dict): A dictionary of user login information.
    """
    __file_path = "user_logins.json"
    __logins = {}

    def __init__(self):
        self.load_logins()

    def load_logins(self):
        """Load user login information from the file."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                self.__logins = json.load(f)
        except FileNotFoundError:
            pass

    def save_logins(self):
        """Save user login information to the file."""
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(self.__logins, f)

    def add_login(self, username, password):
        """Add a user login.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.__logins[username] = password
        self.save_logins()

    def check_login(self, username, password):
        """Check if a user login is valid.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        stored_password = self.__logins.get(username)
        return stored_password == password

    def remove_login(self, username):
        """Remove a user login.

        Args:
            username (str): The username of the user to remove.
        """
        if username in self.__logins:
            del self.__logins[username]
            self.save_logins()

    def get_all_logins(self):
        """Get a dictionary of all user logins.

        Returns:
            dict: A dictionary where keys are usernames and values are passwords.
        """
        return self.__logins

if __name__ == "__main__":
    # Example usage:
    storage = FileStorage()

    # Adding user logins
    storage.add_login("user1", "password1")
    storage.add_login("user2", "password2")

    # Checking if a login is valid
    is_valid = storage.check_login("user1", "password1")
    print("Is login valid:", is_valid)

    # Removing a user login
    storage.remove_login("user2")

    # Getting all user logins
    all_logins = storage.get_all_logins()
    print("All user logins:", all_logins)
