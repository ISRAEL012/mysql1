import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="labo",
    database="pydb_demo"
)   
mycursor = db.cursor()

#After creating database 
#We need to create table
mycursor.execute("CREATE TABLE employees (empID INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(40) NOT NULL, last_name VARCHAR(40) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, job_title VARCHAR(40) NOT NULL, hire_date DATE NOT NULL, salary FLOAT CHECK(salary>=15000 AND salary<=50000))")

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(
