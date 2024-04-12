DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    date_publication DATE,
    auteur_prenom TEXT NOT NULL, 
    auteur_nom TEXT NOT NULL
)
