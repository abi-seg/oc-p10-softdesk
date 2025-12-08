from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    peut_etre_contacte = models.BooleanField(default=False)
    partage_donnees = models.BooleanField(default=False)

    def __str__(self):
        return self.username
# Create your models here.
