# Création de la base de données
# CREATE DATABASE zoo;

# Sélection de la base de données
# USE zoo;

# Création de la table "cage"
# CREATE TABLE cage (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     superficie INT,
#     capacite_max INT
# );

# Création de la table "animal"
# CREATE TABLE animal (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     nom VARCHAR(255),
#     race VARCHAR(255),
#     id_cage INT,
#     date_naissance DATE,
#     pays_origine VARCHAR(255),
#     FOREIGN KEY (id_cage) REFERENCES cage(id)
# );

import mysql.connector

class ZooManager:

    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            print("Connexion à la base de données réussie.")
        except mysql.connector.Error as err:
            print(f"Erreur de connexion à la base de données : {err}")

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        try:
            query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
            values = (nom, race, id_cage, date_naissance, pays_origine)
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Animal ajouté avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'ajout de l'animal : {err}")

    def display_all_animals(self):
        try:
            query = "SELECT * FROM animal"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'affichage des animaux : {err}")

    def display_animals_in_cages(self):
        try:
            query = "SELECT c.id AS cage_id, a.* FROM cage c LEFT JOIN animal a ON c.id = a.id_cage"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                print(row)
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'affichage des animaux dans les cages : {err}")

    def calculate_total_cage_superficie(self):
        try:
            query = "SELECT SUM(superficie) FROM cage"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result[0]
        except mysql.connector.Error as err:
            print(f"Erreur lors du calcul de la superficie totale des cages : {err}")

    def close_connection(self):
        try:
            self.cursor.close()
            self.conn.close()
            print("Connexion à la base de données fermée.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la fermeture de la connexion : {err}")

zoo_manager = ZooManager(host="localhost", user="root", password="", database="zoo")
if zoo_manager.conn.is_connected():
    zoo_manager.cursor.execute("INSERT INTO cage (superficie, capacite_max) VALUES (100, 5)")
    zoo_manager.conn.commit()

    zoo_manager.add_animal("Lion", "Félin", 1, "2022-01-01", "Afrique")
    zoo_manager.add_animal("Panda", "Ours", 2, "2022-02-01", "Asie")

    zoo_manager.display_all_animals()
    zoo_manager.display_animals_in_cages()

    superficie_totale = zoo_manager.calculate_total_cage_superficie()
    if superficie_totale is not None:
        print(f"La superficie totale de toutes les cages est de {superficie_totale} m2")

    zoo_manager.close_connection()