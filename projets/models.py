from django.db import models
from utilisateurs.models import Utilisateur
import uuid

class Projet(models.Model):
    TYPE_CHOICES = [
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='projets')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Contributeur(models.Model):
    """Modèle représentant un contributeur à un projet."""
    ROLE_CHOICES = [
        ('AUTEUR', 'Auteur'),
        ('CONTRIBUTEUR', 'Contributeur'),
    ]
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CONTRIBUTEUR')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.projet.titre} ({self.role})"
    
    class Meta:
        unique_together = ('utilisateur', 'projet')
    
class Probleme(models.Model):
        """Modèle représentant un problème dans un projet."""

        BALISE_CHOICES = [
            ('BUG', 'Bug'),
            ('FEATURE','Fonctionnalité'),
            ('TASK', 'Tâche'),  
        ]
      
        PRIORITE_CHOICES = [
            ('LOW', 'Faible'),
            ('MEDIUM', 'Moyenne'),
            ('HIGH', 'Haute'),
        ]
        STATUT_CHOICES = [
            ('TODO', 'À faire'),
            ('IN_PROGRESS', 'En cours'),
            ('FINISHED', 'Terminé'),
        ]
        titre = models.CharField(max_length=255)
        description = models.TextField()
        balise = models.CharField(max_length=10, choices=BALISE_CHOICES)
        priorite = models.CharField(max_length=10, choices=PRIORITE_CHOICES)
        statut = models.CharField(max_length=15, choices=STATUT_CHOICES, default='TODO')
        projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='problemes')
        auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='problemes_crees')
        assigne_a = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, 
                                      related_name='problemes_assignes')
        date_creation = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.titre} ({self.balise})"

class Commentaire(models.Model):
    """Modèle représentant un commentaire sur un problème."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    probleme = models.ForeignKey('Probleme', on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='commentaires')

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur.username} sur {self.probleme.titre}"
