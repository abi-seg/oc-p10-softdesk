# SoftDesk - API RESTful avec Django REST Framework

Présentation:
  SoftDesk est une application de suivi de projets et de bugs développée avec Django et Django REST Framework.  
  Ce projet permet aux utilisateurs de:
     Créer des projets, 
     Ajouter des contributeurs à chaque projet, 
     Signaler des problèmes (issues), et 
     Ajouter des commentaires collaboratifs sur les issues.

Technologies utilisées:
  Python 3.10+
  Django 4.x
  Django REST Framework
  Pipenv
  SQLite
  Postman(pour tests API)

Prérequis:
  Python installé (v3.10 ou plus)
  pipenv installé (pip install --user pipenv)
  git

Fonctionnalités

-  Authentification sécurisée via **JWT** (DRF simpleJWT)
-  Modèle utilisateur personnalisé (Utilisateur)
- Création, modification et suppression de projets
- Gestion des contributeurs (ajout/suppression)
- Création d’issues liées à un projet
- Interface de commentaires sur les issues
- Routes imbriquées (Nested Routing)
- Permissions basées sur les rôles (auteur, contributeur)
- Pagination automatique avec DRF

Configuration initiale du projet

  Cloner le dépot:
    ```
    git clone https://github.com/abi-seg/oc-p10-softdesk.git
    cd softdesk-api

1. Créer l'environment avec pipenv
    ```bash
     pipenv install --python 3.10
     pipenv install django djangorestframework
     pipenv shell

3. Initialiser le projet Django
     django-admin startproject softdesk .

4. Créer les applications Django
     python manage.py startapp utilisateurs
     python manage.py startapp projets

5. Ajouter les apps dans settings.py
     dans softdesk/settings.py, ajouter dans INSTALLED_APPS:
       INSTALLED_APPS = [
                  .....
                 'rest_framework',
                 'utilisateurs',
                 'projets',
           ]

6. Définir le modèle utilisateur personnalisé
   
   Dans settings.py, ajouter :
    AUTH_USER_MODEL = 'utilisateurs.Utilisateur'

7. Appliquer les migrations
     python manage.py migrate

8. Créer un superutilisateur
     python manage.py createsuperuser

9. Lancer le serveur
     python manage.py runserver
       Le projet sera disponible à l'adresse : http://127.0.0.1:8000
       Connectez-vous à l’admin sur http://127.0.0.1:8000/admin
     
10. Routes principales de l’API

Endpoints	  
      
/api/projects/	--> CRUD projets
/api/projects/<id>/contributors/ --> Gérer les membres
/api/projects/<id>/issues/ --> Gérer les bugs
/api/projects/<id>/issues/<id>/comments/ -->	Gérer les commentaires
/api/users/ --> Lecture des utilisateurs   
     
11. Authentification JWT
     
     POST /api/token/ → Connexion
     POST /api/token/refresh/ → Rafraîchissement du token

Toutes les routes sont sécurisées et nécessitent un token Bearer dans le header Authorization.
   
