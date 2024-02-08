import sqlite3

connection = sqlite3.connect("pupil.db")

command = """
SELECT * from pupils ORDER BY age;
"""

cursor = connection.cursor()

cursor.execute(command)

pupils = cursor.fetchall()

# print(pupils)

command = """
SELECT DISTINCT class from pupils ;
"""
cursor.execute(command)

sinflar = cursor.fetchall()

# print(f"Bizda o'yiyotkan o'quvchilar sinflari:{sinflar}")

#eng yosh o'quvchilar

command = """
SELECT *, MIN(age) from pupils;
"""
cursor.execute(command)
eng_yosh_oquvchi = cursor.fetchall()
print(eng_yosh_oquvchi)


