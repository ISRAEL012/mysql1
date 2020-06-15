import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="labo",
    database="pydb_demo"
)   
mycursor = db.cursor()

# To insert some employees in the table

sql = "INSERT INTO employees (first_name, last_name, email, job_title, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"

val = [
    ("Darmin", "Feras", "dar@gmail.com", "Secretary", "1995-02-28", 22284.39), 
    ("Alex", "Son", "alex-so@gmail.com", "Developer", "2005-06-21", 30453.59), 
    ("Tamar", "mue", "tama@gmail.com", "Supervisor", "2016-08-17", 23000.83), 
    ("Sera", "Zoe", "sez@gmail.com", "Administrator", "1991-12-04", 46783.04),
    ("rene", "Labo", "rene@gmail.com", "Manager", "1998-05-02", 38089.78)
]
mycursor.executemany (sql, val)

db.commit()

print(mycursor, "was inserted")
