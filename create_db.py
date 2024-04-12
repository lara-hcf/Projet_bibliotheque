import sqlite3

connection= sqlite3.connect('database2.db')

with open('schemas.sql') as f:
    connection.executescript(f.read())

cur= connection.cursor()

cur.execute("INSERT INTO livres (titre,auteur_prenom, auteur_nom) VALUES (?,?,?)", ('Chez le roi merlin','Arthur','Jean'))

connection.commit()
connection.close()