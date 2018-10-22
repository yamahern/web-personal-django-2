from django.contrib import admin

# Register your models here.
from .models import Project

# ESTA CLASE ES PARA MOSTRAR LOS ATRIBUTOS created y updated DEL MODELO Project EN EL DJANGO ADMIN
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# ESTO ES PARA QUE SE MUESTREN LAS TABLAS(MODELOS) EN DJANGO ADMIN
admin.site.register(Project, ProjectAdmin)
