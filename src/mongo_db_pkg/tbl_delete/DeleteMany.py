import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")