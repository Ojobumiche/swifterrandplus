from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base

class UserLogin(Base):
    """Represents a user login in the database."""
    __tablename__ = 'user_logins'

    username = Column(String(255), primary_key=True)
    password = Column(String(255), nullable=False)

class DBStorage:
    """Represents a database storage engine for user logins.

    Attributes:
        __engine (Engine): The database engine.
        __session (Session): The database session.
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://<username>:<password>@<host>/<database>')
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def add_login(self, username, password):
        """Add a user login to the database.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        new_login = UserLogin(username=username, password=password)
        self.__session.add(new_login)
        self.__session.commit()

    def check_login(self, username, password):
        """Check if a user login is valid.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the login is valid, False otherwise.
        """
        user_login = self.__session.query(UserLogin).filter_by(username=username, password=password).first()
        return user_login is not None

    def remove_login(self, username):
        """Remove a user login from the database.

        Args:
            username (str): The username of the user to remove.
        """
        user_login = self.__session.query(UserLogin).filter_by(username=username).first()
        if user_login:
            self.__session.delete(user_login)
            self.__session.commit()

if __name__ == "__main__":
    # Example usage:
    storage = DBStorage()

    # Adding user logins
    storage.add_login("user1", "password1")
    storage.add_login("user2", "password2")

    # Checking if a login is valid
    is_valid = storage.check_login("user1", "password1")
    print("Is login valid:", is_valid)

    # Removing a user login
    storage.remove_login("user2")
