# mongo1.py
from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient()
# data base name : 'test-database-1'
mydb = client['test-database-1']

import datetime

myrecord1 = {
    "author": "Duke",
    "title" : "PyMongo 101",
    "tags" : ["MongoDB", "PyMongo", "Tutorial"],
    "date" : datetime.datetime.utcnow()
    }

record_id = mydb.mytable.insert(myrecord1)

myrecord2 = {
    "author" : "Shravan Kumar",
    "title" : "Dr.",
    "tags" : ["Ph.D.", "Machine Learning", "Computer Vision", "Deep Learning"],
    "date" : datetime.datetime.utcnow()
}

record_id = mydb.myinfo.insert(myrecord2)

print record_id
print mydb.collection_names()
print("\n")
print(myrecord1)
print("\n")
print("{}{}".format(myrecord2["title"],myrecord2["author"]))
print mydb["test-database-1"]["myrecord1"]["author"]
