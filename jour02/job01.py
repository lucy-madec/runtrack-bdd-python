import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)

cursor = conn.cursor()

# Exécution de la requête pour récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Affichage du résultat sur le terminal
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
