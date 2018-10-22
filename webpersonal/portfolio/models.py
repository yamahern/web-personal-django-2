# TIPOS DE CAMPO: (xField) https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
# OPCIONES DE CAMPO: (xField) https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-options
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')  
    # upload_to : ES PARA QUE SE LE INDIQUE DONDE GUARDAR LAS IMAGENES  |  'nombre de directorio' 
    # El DIRECTORIO O CARPETA SE CREARA AUTOMATICAMENTE DENTRO DE LA CARPETA media
    link = models.URLField(verbose_name='Direccion Web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    # verbose_name : ES PARA TRADUCIR LOS CAMPOS A ESPAÑOL O CAMBIARLE EL NOMBRE

    class Meta:
        verbose_name = 'proyecto'  
        verbose_name_plural = 'proyectos'
        ordering = ['-created']  # ORDENA DEL MAS NUEVO AL MAS ANTIGUO

    def __str__(self):
        return self.title


