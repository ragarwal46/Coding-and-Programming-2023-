import pyodbc

# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SHIVSQL2019ENT;DATABASE=StudentDB;Trusted_Connection=yes;')

cursor=connection.cursor()
cursor.execute("SELECT * from Student")

for i in cursor:
    print(i)

cursor.close()
connection.close()