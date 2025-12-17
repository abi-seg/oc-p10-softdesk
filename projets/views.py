from rest_framework import viewsets, permissions, serializers
from .models import Project, Contributor, Utilisateur, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, commentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
       return Project.objects.all()
    
    def perform_create(self, serializer):
       serializer.save(author=self.request.user) # save author as project creator

        

class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        return Contributor.objects.select_related('project', 'user').filter(project_id=self.kwargs['project_pk'])   
    
    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_pk'])
        user_id = self.request.data.get('user')
        user = Utilisateur.objects.get(pk=user_id)

        
        if Contributor.objects.filter(project=project, user=user).exists():
                raise serializers.ValidationError("This user is already a contributor to the project.")
            
        serializer.save(project=project, user=user)
      
        
class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.select_related('project', 'author', 'assigned_to').filter(project_id=project_id)

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['project_pk'])
        assigned_to_id = self.request.data.get('assigned_to')
        assigned_to = Utilisateur.objects.get(pk=assigned_to_id) if assigned_to_id else None

        # Ensure only project author can create issues

        if project.author != self.request.user:
                raise serializers.ValidationError("You are not the author of this project.")

        serializer.save(project=project, author=self.request.user, assigned_to=assigned_to)
            
        
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = commentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Comment.objects.all()
        
        return Comment.objects.select_related('issue', 'author').filter(issue_id=self.kwargs['issue_pk'])
    
    def perform_create(self, serializer):
       
            issue = Issue.objects.get(pk=self.kwargs['issue_pk'])

            serializer.save(issue=issue, author=self.request.user)
        