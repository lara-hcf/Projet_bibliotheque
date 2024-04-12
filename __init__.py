from flask import Flash, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app= Flask(__name__)


@app.route('/')
def menu():
    return "<h1>Page d'acceuil</h1>"

@app.route('/enregistrerLivre')
def enregister():
    return render_template("enregistrer_livre.html")

if __name__ == "__main__":
    app.run(debug=True)