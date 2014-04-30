import pymongo
import pymongo.errors

client = pymongo.MongoClient("localhost", 27017)
db = client.lifelogger_notebook
[db.drop_collection(collection) for collection in set(db.collection_names()) - {"system.indexes"}]
print("Current collections: {}".format(db.collection_names()))

def db_setup(db):
    global users
    users = db.create_collection("users")
    users.create_index([("email", pymongo.HASHED)], safe=True)
    users.create_index([("username", pymongo.HASHED)], safe=True)

    global sheets
    sheets = db.create_collection("sheets")

db_setup(db)