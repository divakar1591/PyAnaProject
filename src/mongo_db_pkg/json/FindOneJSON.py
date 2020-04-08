import pymongo
import json

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

x = mycol.find_one()
print(type(x))
jsn = json.dumps(x)
print(jsn.find())
