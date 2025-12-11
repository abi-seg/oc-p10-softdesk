from rest_framework import viewsets, permissions, serializers
from .models import Project, Contributor, Utilisateur, Issue
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            return Project.objects.none()
        
        # Admin see all projects
        if user.is_staff or user.is_superuser:
            return Project.objects.all()
        
        # Regular users see only their projects
        return Project.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
       serializer.save(author=self.request.user) # save author as project creator

        

class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Contributor.objects.all()
        
        return Contributor.objects.filter(project__author=self.request.user) | Contributor.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        user_id = self.request.data.get('user')

        try:
            project = Project.objects.get(id=project_id)
            user = Utilisateur.objects.get(id=user_id)

            if Contributor.objects.filter(project=project, user=user).exists():
                raise serializers.ValidationError("This user is already a contributor to the project.")
            
            serializer.save(project=project, user=user)
        except (Project.DoesNotExist, Utilisateur.DoesNotExist):
            raise serializers.ValidationError("Invalid user or project ID.")
        
class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Issue.objects.all()
        
        return Issue.objects.filter(project__author=self.request.user) | Issue.objects.filter(assigned_to=self.request.user)
    
    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        assigned_to_id = self.request.data.get('assigned_to')

        try:
            project = Project.objects.get(id=project_id)
            assigned_to = Utilisateur.objects.get(id=assigned_to_id) if assigned_to_id else None

            if project.author != self.request.user:
                raise serializers.ValidationError("You are not the author of this project.")

            serializer.save(project=project, author=self.request.user, assigned_to=assigned_to)
        except (Project.DoesNotExist, Utilisateur.DoesNotExist):
            raise serializers.ValidationError("Invalid project or assignee ID.")