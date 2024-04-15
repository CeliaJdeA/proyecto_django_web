from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Nacionalidade(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese las nacionalidades de las jugadoras")
    def __str__(self):
        return self.nombre

class Posicione (models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese las posiciones de las jugadoras",default="Sin posición")
    def __str__(self):
        return self.nombre

class Categoria (models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingrese las categorias de las jugadoras",default="Sin categoría")
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('detalles', args=[str(self.id)])

class Jugadora(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    numero = 
    posicion = models.ForeignKey(Posicione, on_delete=models.SET_NULL, null=True)
    nacionalidad = models.ForeignKey(Nacionalidade, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalles', args=[str(self.id)])

