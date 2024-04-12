import sqlite3

connection= sqlite3.connect('database2.db')

with open('schemas.sql') as f:
    connection.executescript(f.read())

cur= connection.cursor()

cur.execute("INSERT INTO livres (titre,auteur_nom,nb_exemplaire) VALUES (?,?,?)", ('Chez le roi merlin','Jean de la fontaine','15'))

connection.commit()
connection.close()