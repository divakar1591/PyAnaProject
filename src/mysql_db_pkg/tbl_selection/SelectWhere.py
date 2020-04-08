import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sangam@123ABC",
  database="mydatabase"

)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers WHERE id = 25") # Reation operator(id > 25, id < 25, id = 25, id != 24, id >= 25, id <= 25)
# mycursor.execute("SELECT * FROM customers WHERE address = 'Park Lane 38'")
mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'") #wildcard


# Check w3school SQL tutorial for more query

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
