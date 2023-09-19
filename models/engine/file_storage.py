#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from importlib import import_module
import os

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ Initializes a file storage instances """
        self.model_classes = {
                    'BaseModel': import_module('models.base_model').BaseModel, 
                    'User': import_module('models.user').User, 
                    'Place': import_module('models.place').Place,
                    'State': import_module('models.state').State, 
                    'City': import_module('models.city').City, 
                    'Amenity': import_module('models.amenity').Amenity,
                    'Review': import_module('models.review').Review
                  }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    dict[key] = value
                return dict
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = self.model_classes
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.__objects[key] = classes[val[key]['__class__']](**val[key])
        except:
            pass

    def delete(self, obj=None):
        """  delete obj from __objects if it’s inside """
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects:
                del self.__objects[obj_key]
