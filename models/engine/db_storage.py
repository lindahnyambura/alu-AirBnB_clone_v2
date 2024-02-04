#!/usr/bin/python3
"""
This script defines a class DBStorage to handle database connections, SQL commands, and interactions with models using SQLAlchemy
"""
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.exc import InvalidRequestError
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    DBStorage class to handle database connections, SQL commands, and interactions with models using SQLAlchemy
    """
    __engine = None
    __session = None
    def __init__(self) -> None:
        """
        Initializes the DBStorage instance and establishes a connection to the MySQL database using SQLAlchemy
        """
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database_name = getenv("HBNB_MYSQL_DB")
        database_url = "mysql+mysqldb://{}:{}@{}/{}".format(username,
                                                            password,
                                                            host,
                                                            database_name)
        self.__engine = create_engine(database_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects of a specified class or all objects if class is not specified.
        """
        objs_list = []
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objs_list = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objs_list.extend(self.__session.query(subclass).all())
        obj_dict = {}
        for obj in objs_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """
        Adds a new object to the database session
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """"
        Commits changes to the database session
        """
        self.__session.commit()    
      
    def delete(self, obj=None):
        """
        deletes  the specified object from the database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads the database session and recreates all tables
        """
        Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()