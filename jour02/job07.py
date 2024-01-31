# Création de la nouvelle base de données
# CREATE DATABASE ma_base_de_donnees;
# Sélection de la nouvelle base de données
# USE ma_base_de_donnees;
# -- Création de la table "employe"
# CREATE TABLE employe (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     nom VARCHAR(255),
#     prenom VARCHAR(255),
#     salaire DECIMAL(10, 2),
#     id_service INT
# );
# -- Insérer des employés dans la table "employe"
# INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Lamorte', 'Vanny', 3500.00, 1);
# INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Lorquet', 'Ines', 4000.00, 2);
# INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Iribaren', 'Lucas', 3000.00, 3);
# INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Martinie', 'Lucas', 2800.00, 4);
# -- Récupérer les employés avec un salaire supérieur à 3 000 €
# SELECT * FROM employe WHERE salaire > 3000;

# -- Ajouter la table "service"
# CREATE TABLE service (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     nom VARCHAR(255)
# );

# -- Insérer des services dans la table "service"
# INSERT INTO service (nom) VALUES ('Dev Web');
# INSERT INTO service (nom) VALUES ('IA');
# INSERT INTO service (nom) VALUES ('Cybersecurite');
# INSERT INTO service (nom) VALUES ('Dev Logiciel');

# -- Récupérer tous les employés et leur service respectif
# SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS nom_service
# FROM employe e
# JOIN service s ON e.id_service = s.id;

import mysql.connector

class Employe:

    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def fetch_high_salary_employees(self):
        query = "SELECT * FROM employe WHERE salaire > 3000"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def fetch_all_employees_with_service(self):
        query= """
            SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS nom_service
            FROM employe e
            JOIN service s ON e.id_service = s.id;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(row)
        
    def close_connection(self):
        self.cursor.close()
        self.conn.close()

employe_manager = Employe(host="localhost", user="root", password="", database="laplateforme_jour2")
employe_manager.fetch_high_salary_employees()
employe_manager.fetch_all_employees_with_service()
employe_manager.close_connection()
