import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HARISHr@2006",
    database="habit_tracker"
)

print("Connected to MySQL")

connection.cursor().execute("CREATE DATABASE habit_tracker")
connection.cursor().execute("USE habit_tracker")
connection.cursor().execute("SOURCE d:/projects/habitracker/schema.sql")
connection.cursor().execute("SHOW TABLES")


#Get-Content d:\projects\habitracker\schema.sql | mysql -u root -p habit_tracker