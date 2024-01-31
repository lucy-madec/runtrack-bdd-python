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
