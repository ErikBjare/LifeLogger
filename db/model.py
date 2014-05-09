import pymongo
from datetime import datetime

from db import db


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


def model(cls):
    collection_name = cls.__class__.__name__.lower()+"s"
    try:
        coll = db[collection_name]
    except TypeError:
        coll = db.create_collection(cls.__class__.__name__.lower()+"s")
    cls.collection = coll
    return cls


class BaseModel():
    """Baseclass for a MongoDB model"""

    def __init__(self):
        pass

    def create(self, document):
        self.collection.insert(document)

    def save(self):
        """Saves changes to database"""
        self.collection.save(self.data)

    def __str__(self):
        return str(self.data)

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


@model
class User(BaseModel):
    @classmethod
    def new(cls, username, password, email):
        user = cls()
        user.data = {"username": username, "password": password, "email": email}
        user.save()
        print("Created user: ".format(user.data))
        return user


@model
class Sheet(BaseModel):
    """Model for logging-sheets"""

    @classmethod
    def new(cls, user, year=None, month=None, **kwargs):
        sheet = Sheet()
        if year and month:
            d = datetime(year, month, 1)
        elif year or month:
            raise ValueError("You must specify both year and month, or neither.")
        else:
            d = datetime.now()
        sheet.data = sheet.get_document(user, d.year, d.month)
        return sheet

    def get_document(self, user, year, month):
        documents = self.collection.find({"username": user["username"]})
        for document in documents:
            if document and document["year"] == year and document["month"] == month:
                return document
        return self._new_document(user, year, month)

    def set(self):
        raise NotImplemented

    @staticmethod
    def _new_document(user, year, month):
        document = {"username": user["username"],
                    "fields": {},
                    "order": [],
                    "year": year,
                    "month": month}
        return document

    @state_change
    def add_field(self, label, group, datatype="string"):
        if group not in self.data["fields"].keys():
            raise KeyError("Group '{}' did not exist".format(group))
        if label in self.data["fields"][group].keys():
            raise KeyError("Field '{}' already exists".format(group))

        # Implement this as a decorator later
        check_datatype(datatype)

        self.data["fields"][group][label] = {"datatype": datatype}
        group_index = [group for group, _ in self.data["order"]].index(group)
        self.data["order"][group_index][1].append(label)

    @state_change
    def add_group(self, group):
        if group in self.data["fields"]:
            raise KeyError("Group '{}' already exists".format(group))
        self.data["fields"][group] = {}
        self.data["order"].append((group, []))

    @state_change
    def put(self, data: str, field: str, group: str):
        # ToDo: Add date parameter
        self.data["fields"][group][field].append(data)

    @state_change
    def add_3_a_day(self, group):
        self.add_group(group, save=False)
        self.add_field("08:00", group, save=False)
        self.add_field("12:00", group, save=False)
        self.add_field("20:00", group, save=False)

    def __repr__(self):
        return str(self.data)