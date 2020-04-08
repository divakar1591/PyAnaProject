import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

x = mycol.find().limit(5)
for y in x:
    print(y)