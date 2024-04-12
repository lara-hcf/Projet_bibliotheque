DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur_nom TEXT NOT NULL,
    nb_exemplaire INTEGER
);
CREATE TABLE Utilisateurs (
    ID_utilisateur INT PRIMARY KEY,
    Nom VARCHAR(255),
    Prenom VARCHAR(255),
    Email VARCHAR(255)
);

CREATE TABLE Emprunts (
    ID_emprunt INT PRIMARY KEY,
    ID_utilisateur INT,
    ID_livre INT,
    Date_emprunt DATE,
    Date_retour_prevue DATE,
    Date_retour_effective DATE,
    FOREIGN KEY (ID_utilisateur) REFERENCES Utilisateurs(ID_utilisateur),
    FOREIGN KEY (ID_livre) REFERENCES Livres(ID_livre)
);