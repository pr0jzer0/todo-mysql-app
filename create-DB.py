import mysql.connector

db = mysql.connector.connect(
    user= "root",
    password= "",
    
)

dbcursor = db.cursor()
# Create a database named 'to_do_list' if it doesn't exist
dbcursor.execute("CREATE DATABASE IF NOT EXISTS to_do_list")
db.database = "to_do_list"

# Create a table named 'newtasklist' with columns for id, Task

dbcursor.execute("CREATE TABLE newtasklist(id INT AUTO_INCREMENT PRIMARY KEY, Task VARCHAR(255))")
print("Table created successfully")