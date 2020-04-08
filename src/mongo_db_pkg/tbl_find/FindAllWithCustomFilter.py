import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

myQuery = { "address": "Lowstreet 27"}

list = mycol.find(myQuery)

for y in list:
    print(y)