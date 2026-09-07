"""
Referencia sobre referenciar el modelo de usuario custom desde otras apps:
https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#referencing-the-user-model
"""
from django.conf import settings
from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    alumno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='calificaciones',
        limit_choices_to={'rol': 'alumno'},
    )
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.alumno} - {self.materia}: {self.valor}'


class Asistencia(models.Model):
    alumno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='asistencias',
        limit_choices_to={'rol': 'alumno'},
    )
    fecha = models.DateField()
    presente = models.BooleanField(default=True)

    class Meta:
        # un alumno no puede tener dos registros de asistencia el mismo día
        unique_together = ('alumno', 'fecha')

    def __str__(self):
        estado = 'presente' if self.presente else 'ausente'
        return f'{self.alumno} - {self.fecha}: {estado}'


class RelacionFamiliar(models.Model):
    """Vincula un padre/tutor con el/los alumno/s a su cargo."""
    padre = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hijos_a_cargo',
        limit_choices_to={'rol': 'padre'},
    )
    alumno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='padres_tutores',
        limit_choices_to={'rol': 'alumno'},
    )

    class Meta:
        unique_together = ('padre', 'alumno')

    def __str__(self):
        return f'{self.padre} -> {self.alumno}'
