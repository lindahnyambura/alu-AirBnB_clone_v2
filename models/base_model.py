#!/usr/bin/python3

from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """Defines the BaseModel class.

    Attributes:
        id (sqlalchemy String): The BaseModel id.
    """

    id = Column(String(60), primary_key=True, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())

    def save(self):
        """Save the instance to the database."""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        return my_dict

    def delete(self):
        """Delete the current instance from storage."""
        from models import storage
        storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.to_dict())

