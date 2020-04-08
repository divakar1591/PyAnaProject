import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

###DB
mydb = myclient["mydatabase"] # Db creation

dblist = myclient.list_database_names()
print(dblist)

if "mydatabase" in dblist:
  print("The database exists.")

###TABLE
  mycol = mydb["customers"] #table creation

  print(mydb.list_collection_names())

  collist = mydb.list_collection_names()
  if "customers" in collist:
    print("The collection exists.")