import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db creation
mycol = mydb["customers"] #table creation

mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)