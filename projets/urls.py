from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register(r'projets', ProjectViewSet, basename='projets')

urlpatterns = [
    path('', include(router.urls)),
]