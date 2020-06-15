import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'labo',
    database = 'pydb_demo'
)

mycursor = db.cursor()

mycursor.execute('DELETE FROM employees WHERE empID=2')

db.commit()

mycursor.execute('SELECT * FROM employees')
for x in mycursor:
    print(x)
