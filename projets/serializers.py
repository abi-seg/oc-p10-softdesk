from rest_framework import serializers
from .models import Project, Contributor, Utilisateur,Issue

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
    
class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset = Utilisateur.objects.all()
    )
    project = serializers.PrimaryKeyRelatedField(
        queryset = Project.objects.all()
        )
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role', 'added_at']
        read_only_fields = ['id', 'added_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username  # Display username instead of ID
        rep['project'] = instance.project.title  # Display project title instead of ID
        return rep
    
class IssueSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=Utilisateur.objects.all(),
        
    )
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all() 
    )

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'author', 'assigned_to', 'project', 'created_at']
        read_only_fields = ['id', 'author',  'created_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.username  # Display author's username
        rep['assigned_to'] = instance.assigned_to.username if instance.assigned_to else None  # Display assignee's username
        rep['project'] = instance.project.title  # Display project title
        return rep