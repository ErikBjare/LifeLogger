from datetime import datetime
import logging

import pymongo

from db import database


def check_datatype(datatype):
    assert datatype in ["string", "number"]


def state_change(func):
    """Decorator to be used for functions in models that change the data and requires a save.

    The keyword argument save can be set to False when calling
    any function decorated with this decorator to prevent saving,
    this is useful in cases where a larger operation which consists
    of smaller changes is carried out."""
    def func_dec(self, *args, save=True, **kwargs):
        func(self, *args, **kwargs)
        if save:
            self.save()
    return func_dec


class BaseModel():
    """Baseclass for a MongoDB model"""

    def __init__(self):
        self.data = None

    def create(self, document):
        self.collection.insert(document)

    def save(self):
        """Saves changes to database"""
        self.collection.save(self.data)

    def __str__(self):
        return str(self.data) if self.data else None

    @classmethod
    def get(cls, **kwargs):
        for id in kwargs:
            doc = cls.collection.find_one({id: kwargs[id]})
            if doc:
                return cls.load(doc)

    @classmethod
    def load(cls, data):
        user = cls()
        user.data = data
        return user

    @classmethod
    def find(cls, **kwargs):
        data = cls.collection.find(kwargs)
        if data:
            return [cls.load(doc) for doc in data]
        else:
            return None

    @classmethod
    def find_one(cls, **kwargs):
        doc = cls.collection.find_one(kwargs)
        if doc:
            return cls.load(doc)
        else:
            return None



