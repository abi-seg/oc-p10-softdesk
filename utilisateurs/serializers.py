from rest_framework import serializers
from .models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'age', 'can_be_contacted', 'can_data_be_shared',]    
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError("L'utilisateur doit avoir au moins 15 ans pour s'inscrire .")
        return value