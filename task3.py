import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'labo',
    database = 'pydb_demo'
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM employees")

result = mycursor.fetchall()

for x in result:
    print(x)
print('**********************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE hire_date > "1994-12-23"')
result1 = mycursor.fetchall()
for y in result1:
    print(y)
print('**************************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE hire_date > "1994-12-23" AND salary > 24000')
result2 = mycursor.fetchall()
for z in result2:
    print(z)
print('******************************************************************************************') 

mycursor.execute('SELECT * FROM employees WHERE hire_date < "2000-05-12" OR first_name = "Alex"')
result3 = mycursor.fetchall()
for a in result3:
    print(a)
print('*********************************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE hire_date > "2000-05-12" OR (first_name = "Alex" AND salary <= 40000)')
result4 = mycursor.fetchall()
for b in result4:
    print(b)
print('************************************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE email LIKE "r%"')
like1 = mycursor.fetchall()
for c in like1:
    print(c) 
print('**************************************************************************************************')

mycursor.execute('SELECT * FROM employees   WHERE last_name LIKE "%n"')
like2 = mycursor.fetchall()
for d in like2:
    print(d)
print('***************************************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE first_name LIKE "%e%"')
like3 = mycursor.fetchall()
for e in like3:
    print(e)
print('****************************************************************************************************') 

mycursor.execute('SELECT * FROM employees WHERE salary < 26000 AND first_name LIKE "%a%"')
where = mycursor.fetchall()
for f in where:
    print(f)
print('****************************************************************************************************') 

mycursor.execute('SELECT * FROM employees WHERE first_name LIKE "%e%" OR hire_date >= "1998-10-04"')
where1 = mycursor.fetchall()
for g in where1:
    print(g)
print('*******************************************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE salary >= 30000 ORDER BY first_name DESC')
where2 = mycursor.fetchall()
for h in where2:
    print(h)
print('*********************************************************************************************************')

mycursor.execute('SELECT * FROM employees WHERE salary >= 30000 ORDER BY first_name ASC')
where3 = mycursor.fetchall()
for j in where3:
    print(j)
print('*********************************************************************************************************')
