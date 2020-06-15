import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'labo',
    database = 'pydb_demo'
)

mycursor = db.cursor()

mycursor.execute('DROP TABLE employees')
