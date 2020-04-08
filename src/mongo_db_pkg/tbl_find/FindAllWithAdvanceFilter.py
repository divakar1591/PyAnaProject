import pymongo

###Connection
myclient =  pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"] # Db
mycol = mydb["customers"] #table

"""
to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier
"""
myQuery1 = { "address": { "$regex": "^S" } }

"""
Regex : To find only the documents where the "address" field starts with the letter "S", use the regular expression
"""
myQuery = { "address": { "$regex": "^S" } }


list = mycol.find(myQuery)

for y in list:
    print(y)