import sqlite3

connection = sqlite3.connect("pupil.db")

command = """
INSERT INTO pupils('first_name','last_name','class','age') 
VALUES('Maqsud', 'Quvondiqov', '7-class', '13'),('Shuxrat',"Hamidov",'10-sinf',16); 

"""

cursor = connection.cursor()

cursor.execute(command)

connection.commit()