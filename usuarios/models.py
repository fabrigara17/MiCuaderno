"""
Referencia oficial sobre extender el modelo de usuario:
https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#extending-the-existing-user-model
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Extiende AbstractUser (que ya trae username, email, password hasheado,
    first_name, last_name, is_active, is_staff, is_superuser) agregando
    los campos propios del negocio: dni y rol.
    """

    class Rol(models.TextChoices):
        DOCENTE = 'docente', 'Docente'
        ALUMNO = 'alumno', 'Alumno'
        PADRE = 'padre', 'Padre/Tutor'
        DIRECTIVO = 'directivo', 'Directivo'
    REQUIRED_FILES = ['email', 'dni', 'rol']

    dni = models.CharField('DNI', max_length=20, unique=True)
    rol = models.CharField('Rol', max_length=10, choices=Rol.choices)

    def __str__(self):
        return f'{self.get_full_name() or self.username} ({self.get_rol_display()})'
