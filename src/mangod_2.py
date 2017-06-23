# mongo2.py
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
mydb1 = client['test-database-1']

import datetime

myrecord2 = [
{
"author": "Duke II",
"title" : "PyMongo II 101",
"tags" : ["MongoDB II", "PyMongo II", "Tutorial II"],
"date" : datetime.datetime.utcnow()
},

{
"author": "Duke III",
"title" : "PyMongo III 101",
"tags" : ["MongoDB III", "PyMongo III", "Tutorial III"],
"date" : datetime.datetime.utcnow()
} ]

mydb1.mytable.insert(myrecord2)
#######################################################
# printing the results
#######################################################
print("-"*30)
print("Displaying the collections in mydb1")
print("-"*30)

print mydb1.collection_names()
print("\n")

print("-"*30)
print("Displaying multiple records")
print("-"*30)

print(myrecord2[0])
print("\n")

print(myrecord2[1].items())
print("\n")

print("-"*30)
print("Displaying the keys and values from myrecord2 record1")
print("-"*30)

for i in myrecord2[0].items():
    print("{}\n".format(i))
print("-"*30)

print("-"*30)
print("Displaying the keys and values from myrecord2 record2")
print("-"*30)

for i in myrecord2[1].items():
    print("{}\n".format(i))
print("-"*30)

# To print the keys of myrecord2
'''
for i in myrecord2[1].keys():
    print("{}\n".format(i))
'''
# To print the values of myrecord2

'''for j in  myrecord2[1].values():
    print("{}\n".format(j) )
'''
