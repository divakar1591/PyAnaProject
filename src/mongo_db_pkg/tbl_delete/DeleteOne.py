import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)