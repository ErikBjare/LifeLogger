__author__ = 'erb'

from db import db
from db.db import *
from db.datatypes import *

from db import model
from db.models import *

from pymongo.errors import CollectionInvalid

for cls in BaseModel.__subclasses__():
    collection_name = cls.__name__.lower()+"s"
    try:
        coll = database.create_collection(collection_name)
        print("Collection '{}' was created".format(collection_name))
    except CollectionInvalid:
        coll = database[collection_name]
    print("Created collection {}".format(collection_name))
    cls.collection = coll
print("Current collections: {}".format(database.collection_names()))
