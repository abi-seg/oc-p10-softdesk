"""
URL configuration for softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import index
from rest_framework.routers import DefaultRouter
from utilisateurs.views import UtilisateurViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

router = DefaultRouter()
router.register(r'users', UtilisateurViewSet, basename='users')


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    
    #App API

    path('api/', include('projets.urls')),  # 
    path('api/', include(router.urls)),  # Include the utilisateur routes

    #Basic Auth login/logout
    path('api-auth/', include('rest_framework.urls')),

    # JWT Auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]