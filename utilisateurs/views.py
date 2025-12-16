from rest_framework.viewsets import ModelViewSet
from .models import Utilisateur 
from .serializers import UtilisateurSerializer
from rest_framework.permissions import IsAuthenticated

class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
