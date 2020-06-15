import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'labo',
    database = 'pydb_demo'
)

mycursor = db.cursor()

mycursor.execute('UPDATE employees SET first_name = "Bellot", last_name = "Camile", email = "bel@gmail.com" WHERE empID=2')

db.commit()

mycursor.execute('SELECT * FROM employees')
for x in mycursor:
    print(x)
