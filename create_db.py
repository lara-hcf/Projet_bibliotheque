import sqlite3

connection= sqlite3.connect('database.db')

with open('schema.sq') as f:
    connection.executescript(f.read())


connection.commit()
connection.close()