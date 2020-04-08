import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

x = mycol.find({},{ "_id": 0, "name": 1, "address": 1 })
# x = mycol.find({},{ "address": 0 })

for y in x:
    print(y)