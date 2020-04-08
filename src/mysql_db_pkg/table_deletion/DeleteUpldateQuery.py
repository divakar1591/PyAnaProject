import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sangam@123ABC",
  database="mydatabase"

)

mycursor = mydb.cursor()

sql_query = "DELETE FROM customers WHERE address = 'Mountain 21'"
# UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'
mycursor.execute(sql_query)

mydb.commit()

print(mycursor.rowcount, "record deleted")
