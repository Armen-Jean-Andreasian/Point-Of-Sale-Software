import sqlite3

connection = sqlite3.connect(database='../Store.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM Products")
result = cursor.fetchall()
print(result)
