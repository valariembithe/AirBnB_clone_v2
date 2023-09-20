#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """ MySQL engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes instances / objects """
        user = os.getenv('HBNB_MYSQL_USER')
        pword= os.getenv('HBNB_MYSQL_PWD')
        host =  os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pword, host, db_name
        )
        self.__engine = create_engine(
                DATABASE_URL,
                pool_pre_ping = True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ 
