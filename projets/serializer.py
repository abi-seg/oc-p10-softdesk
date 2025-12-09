from rest_framework import serializers
from .models import Projet

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = '__all__'
        read_only_fields = ['auteur', 'date_creation']