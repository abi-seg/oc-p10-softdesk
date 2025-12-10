from rest_framework import viewsets, permissions
from .models import Project
from projets.serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            return Project.objects.none()
        return Project.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


