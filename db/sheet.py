from datetime import datetime

import db
from db.model import *

class Sheet(db.Model):
    """Model for logging-sheets"""
    def __init__(self, user, year=None, month=None, **kwargs):
        if "db" in kwargs.keys():
            self.db = kwargs["db"]
        else:
            self.db = db.db
        Model.__init__(self, self.db["sheets"])
        if year and month:
            d = datetime(year, month, 1)
        elif year or month:
            raise ValueError("You must specify both year and month, or neither.")
        else:
            d = datetime.now()
        self.data = self.get_document(user, d.year, d.month)
        
    def get_document(self, user, year, month):
        documents = self.collection.find({"username": user["username"]})
        for document in documents:
            if document and document["year"] == year and document["month"] == month:
                return document
        return self._new_document(user, year, month)
        
    def set(self):
        raise NotImplemented
        
    def _new_document(self, user, year, month):
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
    def put(self, data, field, group):
        # ToDo: Add date parameter
        self.data["fields"][group][field].append(data)
        
    def add_3_a_day(self, group):
        self.add_group(group)
        self.add_field("08:00", group)
        self.add_field("12:00", group)
        self.add_field("20:00", group)
        
    def __repr__(self):
        return str(self.data)