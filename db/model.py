import unittest


def check_datatype(datatype):
    assert datatype in ["string", "number"]


def state_change(func):
    def func_dec(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.save()
    return func_dec


class Model():
    """Baseclass for a MongoDB model"""
    def __init__(self, collection):
        self.collection = collection

    def create(self, document):
        self.collection.insert(document)

    def save(self):
        """Saves changes to database"""
        self.collection.save(self.data)