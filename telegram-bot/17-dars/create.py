import sqlite3

connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

#photo,address,username
command = """
CREATE TABLE IF NOT EXISTS USERS(
first_name TEXT,
last_name TEXT,
phone_number TEXT,
telegram_id NUMBER unique
);
"""

cursor.execute(command)

connection.commit()