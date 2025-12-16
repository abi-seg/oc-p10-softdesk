SoftDesk - API RESTful avec Django REST Framework

Présentation:
  SoftDesk est une application de suivi de projets et de bugs développée avec Django et Django REST Framework.  
  Ce projet permet aux utilisateurs de créer des projets, y ajouter des contributeurs, signaler des problèmes, et commenter.

Technologies utilisées:
  Python 3.10+
  Django 4.x
  Django REST Framework
  Pipenv

Prérequis:
  Python installé (v3.10 ou plus)
  pipenv installé (pip install --user pipenv)
  git

Fonctionnalités

-  Authentification via DRF (Basic Auth)
-  Utilisateur avec modèle personnalisé
-  Création et suppression de projets
-  Gestion des contributeurs par projets
-  Système de suivi d’issues
-  Interface de commentaires sur les issues
-  Routes RESTful nested avec permissions
-  Pagination DRF par défaut

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

Endpoint	  
      
/api/projects/	--> CRUD projets
/api/projects/<id>/contributors/ --> Gérer les membres
/api/projects/<id>/issues/ --> Gérer les bugs
/api/projects/<id>/issues/<id>/comments/ -->	Gérer les commentaires
/api/users/ --> Lecture des utilisateurs   
     
   
