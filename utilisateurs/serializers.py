from rest_framework import serializers
from .models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'age', 'peut_etre_contacte', 'partage_donnees']    

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError("L'utilisateur doit avoir au moins 15 ans pour s'inscrire .")
        return value