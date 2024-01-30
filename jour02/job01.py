import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

# Créer un objet curseur
cursor = conn.cursor()

# Exécuter la requête pour récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Afficher le résultat en console
for row in cursor.fetchall():
    print(row)

# Fermer le curseur et la connexion
cursor.close()
conn.close()
