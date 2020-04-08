import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sangam@123ABC",

)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
