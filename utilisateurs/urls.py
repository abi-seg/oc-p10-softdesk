from django.urls import path, include
from rest_framework.routers import DefaultRouter    
from .views import UtilisateurViewSet

router = DefaultRouter()
router.register(r'users', UtilisateurViewSet, basename='utilisateur')    

urlpatterns = [
    path('', include(router.urls)),
]