import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

list1 = mycol.find().sort("name") # ascending
list = mycol.find().sort("name", -1) # Descending

for x in list:
    print(x)
