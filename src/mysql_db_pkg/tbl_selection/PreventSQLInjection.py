import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sangam@123ABC",
  database="mydatabase"

)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s" # can use - DELETE or any other query in same format
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)

# Check w3school SQL tutorial for more query

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
