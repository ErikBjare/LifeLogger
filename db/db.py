import pymongo
import pymongo.errors

client = pymongo.MongoClient("localhost", 27017)
db = client["lifelogger_notebook"]
[db.drop_collection(collection) for collection in set(db.collection_names()) - {"system.indexes"}]
print("Current collections: {}".format(db.collection_names()))


def register_collection(cls):
    collection = cls().collection
    return collection