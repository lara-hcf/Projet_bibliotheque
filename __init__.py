from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)   


@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/enregistrerLivre', methods=['GET'])
def formulaire_enregistrerLivre():
    return render_template("enregistrer_livre.html")

@app.route('/enregistrerLivre', methods=['POST'])
def enregistrer():
    titre= request.form['titre']
    auteur_nom= request.form['nom']
    auteur_prenom= request.form['prenom']

    conn= sqlite3.connect('database2.db')
    cursor= conn.cursor()

    cursor.execute('INSERT INTO livres (id, titre, auteur_prenom, auteur_nom) VALUES (?,?,?,?)', (100, titre, auteur_prenom, auteur_nom))
    conn.execute()
    conn.close()
    return redirect('/consultationLivre')

@app.route('/consultationLivre')
def readBB():
    conn= sqlite3.connect('database2.db')
    cursor= conn.cursor()
    cursor.execute('SELECT * from livres;')
    data= cursor.fetchall()
    conn.close()
    return render_template('consulter_livres.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)