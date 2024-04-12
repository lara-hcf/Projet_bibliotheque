from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)   


@app.route('/')
def menu():
    return "<h1>Page d'acceuil</h1>"

@app.route('/enregistrerLivre', methods=['POST'])
def formulaire_enregistrerLivre():
    return render_template("enregistrer_livre.html")

@app.route('/enregistrerLivre', methods=['GET'])
def enregistrer():
    titre= request.form['titre']
    auteur_nom= request.form['nom']
    auteur_prenom= request.form['prenom']

    conn= sqlite3.connect('database2.db')
    cursor= conn.cursor()

    cursor.execute('INSERT INTO livres (titre, auteur_prenom, auteur_nom) VALUES (?,?,?)', (titre, auteur_prenom, auteur_nom))
    conn.execute()
    conn.close()
    return redirect('/enregistrerLivre')

if __name__ == "__main__":
    app.run(debug=True)