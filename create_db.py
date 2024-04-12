import sqlite3

connection= sqlite3.connect('database2.db')

with open('schemas.sq') as f:
    connection.executescript(f.read())


connection.commit()
connection.close()