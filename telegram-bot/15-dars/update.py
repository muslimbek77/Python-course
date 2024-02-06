import sqlite3

connection = sqlite3.connect("pupil.db")

command = """
UPDATE pupils SET first_name = 'Sardor', last_name = 'Tuxtapulatov',age='14' WHERE last_name='Turobov';
"""

cursor = connection.cursor()

cursor.execute(command)

connection.commit()