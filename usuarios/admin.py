"""
Referencia: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#a-full-example
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Agregamos dni y rol a los fieldsets que ya trae UserAdmin por defecto
    fieldsets = UserAdmin.fieldsets + (
        ('Datos de la libreta', {'fields': ('dni', 'rol')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos de la libreta', {'fields': ('dni', 'rol')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'dni', 'rol', 'is_staff')
    list_filter = UserAdmin.list_filter + ('rol',)
