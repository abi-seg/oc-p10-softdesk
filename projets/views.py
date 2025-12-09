from rest_framework import viewsets, permissions
from .models import Projet
from projets.serializers import ProjetSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Projet.objects.filter(auteur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)


