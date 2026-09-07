"""
Referencia sobre login_required:
https://docs.djangoproject.com/en/5.2/topics/auth/default/#the-login-required-decorator
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Materia

Usuario = get_user_model()


@login_required
def home(request):
    usuario = request.user
    contexto = {'usuario': usuario}

    if usuario.rol == Usuario.Rol.DOCENTE:
        contexto['materias'] = Materia.objects.all()

    elif usuario.rol == Usuario.Rol.ALUMNO:
        contexto['calificaciones'] = usuario.calificaciones.select_related('materia').all()
        contexto['asistencias'] = usuario.asistencias.order_by('-fecha')[:10]

    elif usuario.rol == Usuario.Rol.PADRE:
        relaciones = usuario.hijos_a_cargo.select_related('alumno').all()
        contexto['hijos'] = [r.alumno for r in relaciones]

    elif usuario.rol == Usuario.Rol.DIRECTIVO:
        contexto['total_alumnos'] = Usuario.objects.filter(rol=Usuario.Rol.ALUMNO).count()
        contexto['total_docentes'] = Usuario.objects.filter(rol=Usuario.Rol.DOCENTE).count()

    return render(request, 'academico/home.html', contexto)
