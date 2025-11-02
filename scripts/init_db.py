import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS neuralearn;")
print("? Database 'neuralearn' created or already exists.")

cursor.close()
connection.close()
