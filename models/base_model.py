#!/usr/bin/python3
"""Defines the BaseModel class."""
from models import base_model
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base model of the swifterrand+."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs of attributes.
        """
        timestamp_format = "%Y-%m-%dT%H:%M:%S.%f"

        # Initialize id, created_at, and updated_at attributes
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Populate attributes from kwargs, if provided
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, timestamp_format))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Updates the 'updated_at' attribute with
        the current datetime and saves the model."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair '__class__' representing
        the class name of the object.
        """
        result = {
            **self.__dict__,
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "__class__": self.__class__.__name__
        }
        return result

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.to_dict()
        )
