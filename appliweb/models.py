from django.db import models

class Sujet(models.Model):
    TYPE_SUJET_CHOICES = [
        ('TD', 'Travaux Dirigés'),
        ('TPE', 'Travaux Pratiques Encadrés'),
        ('CC', 'Contrôle Continu'),
        ('EXAM', 'Examen'),
    ]
    NIVEAU_CHOICES = [
        ('Niveau 1', 'Niveau 1'),
        ('Niveau 2', 'Niveau 2'),
        ('Niveau 3', 'Niveau 3'),
    ]
    FILIERE_CHOICES = [
        ('Informatique Fondamentale', 'Informatique Fondamentale'),
        ('Informatique et Gestion des entreprises', 'Informatique et Gestion des entreprises'),
        ('Mathématiques', 'Mathématiques'),
        ('Physique', 'Physique'),
        ('Chimie', 'Chimie'),
        ('Science Biologie', 'Science Biologie'),
        ('Science de la terre', 'Science de la terre'),

    ]
    
    nom_cours = models.CharField(max_length=100,)
    code_cours = models.CharField(max_length=10)
    titre = models.CharField(max_length=200)
    type_sujet = models.CharField(max_length=4, choices=TYPE_SUJET_CHOICES)
    annee = models.IntegerField()
    niveau = models.CharField(max_length=10, choices=NIVEAU_CHOICES)
    filiere = models.CharField(max_length=100, choices=FILIERE_CHOICES)
    cours = models.CharField(max_length=100, default='Cours')
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return f"{self.code_cours} - {self.nom_cours} : {self.titre} ({self.get_type_sujet_display()})"
