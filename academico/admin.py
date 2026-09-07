from django.contrib import admin

from .models import Asistencia, Calificacion, Materia, RelacionFamiliar

admin.site.register(Materia)
admin.site.register(Calificacion)
admin.site.register(Asistencia)
admin.site.register(RelacionFamiliar)
