-- Sélection de la base de données
USE LaPlateforme;
-- Création de la table etage
CREATE TABLE etage (
    -> id INT PRIMARY KEY AUTO_INCREMENT,
    -> nom VARCHAR(255),
    -> numero INT,
    -> superficie INT
    -> );
-- Création de la table salle
CREATE TABLE salle (
    -> id INT PRIMARY KEY AUTO_INCREMENT,
    -> nom VARCHAR(255),
    -> id_etage INT,
    -> capacite INT
    -> );
-- Vérification de l'ajout des tables
SHOW TABLES;