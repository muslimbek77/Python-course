import sqlite3

connection = sqlite3.connect("pupil.db")

command = """
CREATE TABLE IF NOT EXISTS pupils (
    first_name TEXT,
    last_name TEXT,
    email TEXT unique,
    class TEXT,
    age NUMBER
); 
"""
cursor = connection.cursor()

cursor.execute(command)

connection.commit()