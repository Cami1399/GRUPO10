
# Create your models here.
from django.db import models


class Presentacion(models.Model):
    Presentacion = models.CharField(max_length=20,  null=True)

    def __str__(self):
        return f'{self.Presentacion} '

class Categoria (models.Model):
    Categoria = models.CharField(max_length=50,  null=True)

    def __str__(self):
        return f'{self.Categoria} '

class Libro(models.Model):

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=20)
    Presentacion = models.ForeignKey(Presentacion, on_delete=models.SET_NULL, null=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_publicacion = models.DateField()
    sinopsis = models.TextField()
    disponibilidad = models.BooleanField(default=True)



    def __str__(self):
        return f'{self.id} - {self.titulo}'

