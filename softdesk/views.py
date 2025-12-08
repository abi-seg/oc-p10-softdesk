from django.http import JsonResponse

def index(request):

    return JsonResponse({
        "message": "Bienveneu sur l'API Softdesk!",
        "docs": "Explorez les utilisateurs via /api/utilisateurs/"
        })