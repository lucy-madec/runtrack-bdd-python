INSERT INTO etudiant (nom, prenom, age, email)
VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
SELECT * FROM etudiant; -- Vérification que le nouvel étudiant a bien été ajouté.
SELECT * FROM etudiant WHERE nom = 'Dupuis'; -- Affichage des étudiants du même 'nom'.