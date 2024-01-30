import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

# Création d'un objet curseur
cursor = conn.cursor()

# Exécution de la requête pour récupérer l'ensemble des étudiants
query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

# Affichage du résultat dans le terminal
print("Noms et capacités des salles :")
for row in cursor.fetchall():
    print(f"Nom: {row[0]}, Capacité: {row[1]}")

cursor.close()
conn.close()