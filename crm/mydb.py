import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm-sql")

print("All Done")