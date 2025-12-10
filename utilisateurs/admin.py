from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    model = Utilisateur
    list_display = ('username', 'age', 'can_be_contacted', 'can_data_be_shared', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('age', 'can_be_contacted', 'can_data_be_shared'),
        }),
    )

# Register your models here.
