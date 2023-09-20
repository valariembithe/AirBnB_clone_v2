#!/usr/bin/python3
"""This module defines the DBStorage engine for HBNB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages the database storage for HBNB"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the database"""
        obj_dict = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query_result = self.__session.query(cls).all()
        else:
            query_result = []
            for c in classes:
                query_result.extend(self.__session.query(c).all())

        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add a new object to the database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
