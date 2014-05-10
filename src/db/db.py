import pymongo
import pymongo.errors

client = pymongo.MongoClient("localhost", 27017)
database = client["lifelogger_notebook"]
[database.drop_collection(collection) for collection in set(database.collection_names()) - {"system.indexes"}]
print("Current collections: {}".format(database.collection_names()))