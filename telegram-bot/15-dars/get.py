import sqlite3

connection = sqlite3.connect("pupil.db")

command = """
SELECT * from pupils ORDER BY age;
"""

cursor = connection.cursor()

cursor.execute(command)

pupils = cursor.fetchall()

print(pupils)

