from django.db import models

# Create your models here.

class Libro(models.Model): ### En Django, las clases de modelos heredan de models.Model para indicar que son modelos de bases de datos.
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
