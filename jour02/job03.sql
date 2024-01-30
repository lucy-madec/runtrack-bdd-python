-- Ajout des données de la table etage
INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500);

INSERT INTO etage (nom, numero, superficie) VALUES ('R+1', 1, 500);

-- Ajout des données de la table salle
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Lounge', 1, 100);

INSERT INTO salle (nom, id_etage, capacite) VALUES ('Studio son', 1, 5);

INSERT INTO salle (nom, id_etage, capacite) VALUES ('Broadcasting', 2, 50);

INSERT INTO salle (nom, id_etage, capacite) VALUES ('Bocal pPeda', 2, 4);

INSERT INTO salle (nom, id_etage, capacite) VALUES ('Coworking', 2, 80);

INSERT INTO salle (nom, id_etage, capacite) VALUES ('Studio Video', 2, 5);

-- Exportation de la base de données :
-- Ouverture du Terminal cmd en tant qu'administrateur.
-- cd C:\Program Files\MySQL\MySQL Server 8.0\bin
-- mysqldump -u root -p LaPlateforme > C:\Users\laplateforme03.sql
-- Entrée du mot de passe et ajout du fichier laplateforme.sql dans le VS Studio Code