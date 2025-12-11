from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True) #display author's username
    class Meta:
        model = Project
        fields = ['id','title', 'description', 'type', 'author', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

    def validate_title(self, value):
        user = self.context['request'].user
        if Project.objects.filter(title=value, author=user).exists():
            raise serializers.ValidationError("You already have a project with this title.")    
        return value