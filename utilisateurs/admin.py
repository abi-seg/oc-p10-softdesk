from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    model = Utilisateur
    list_display = ('username', 'age', 'peut_etre_contacte', 'partage_donnees', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('age', 'peut_etre_contacte', 'partage_donnees')
        }),
    )

# Register your models here.
