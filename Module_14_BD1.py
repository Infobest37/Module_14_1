import sqlite3
import random

connection = sqlite3.connect("db.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL, 
email TEXT NOT NULL,
age INTEGER NOT NULL)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", ("newuser","es@mail.ru","28"))
for i in range(100):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"{i}es@mail.ru",
         str(random.randint(28,60))))
# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29,"newuser"))
# cursor.execute("DELETE FROM Users WHERE age")
# cursor.execute("SELECT * FROM Users") # Селект умеет что то получать
# cursor.execute("SELECT username, age FROM Users WHERE age < ?", ("30",) )
# cursor.execute("SELECT age FROM Users GROUP BY AGE ")
cursor.execute("SELECT COUNT (*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(age) FROM Users")
total_age = cursor.fetchone()[0]
cursor.execute("SELECT AVG(age) FROM Users")
avg_age = cursor.fetchone()[0]
print(total_users, total_age, avg_age)

print(total_users)
print(total_age)
print(total_age/total_users)


cursor = cursor.fetchall()
for row in cursor:
    print(row)
connection.commit()
connection.close()
