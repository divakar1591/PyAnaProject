import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sangam@123ABC",
  database="mydatabase"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers") # SELECT name, address FROM customers (to SELECT column)
# Check w3school SQL tutorial for more query

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
