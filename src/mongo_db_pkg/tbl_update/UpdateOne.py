import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)