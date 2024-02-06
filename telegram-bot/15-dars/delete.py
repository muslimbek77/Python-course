import sqlite3

connection = sqlite3.connect("pupil.db")

command = """
DELETE FROM pupils WHERE first_name = 'Sardor';
"""

cursor = connection.cursor()

cursor.execute(command)

connection.commit()