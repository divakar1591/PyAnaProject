import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sangam@123ABC",
  database="mydatabase"

)

mycursor = mydb.cursor()

sql_query = "INSERT INTO customers (name, address) VALUES(%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql_query, val)

mydb.commit()

print(mycursor.rowcount, "inserted successfully")
