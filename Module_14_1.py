import sqlite3
import random

connection = sqlite3.connect("bd1.db")
cursor = connection.cursor()
count = 1
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL, 
email TEXT NOT NULL,
age INTEGER NOT NULL, 
balance INTEGER NOT NULL)
''')
#
k=0
for i in range(1, 11, 1):
      i*=10
      k+=1
      cursor.execute(
         "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
         (f"username{k}", f"es{k}@mail.ru", f"{i}", 1000)
      )

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 != 0")
cursor.execute("DELETE FROM Users WHERE id = 1")
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
# cursor.execute("DELETE FROM Users WHERE id")

# cursor.execute("SELECT * FROM Users") # Селект умеет что то получать
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# cursor.execute("SELECT age FROM Users GROUP BY AGE ")


cursor = cursor.fetchall()
for row in cursor:
     print(row)
connection.commit()
connection.close()