from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre Fabricante")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')
    def __str__(self):
        return self.nombre


class DirectorEjecutivo(models.Model):
    fabricante = models.OneToOneField("Fabricante", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, verbose_name="Director Ejecutivo")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')
    def __str__(self):
        return self.nombre
    

COMBUSTIBLE_CHOICES = [
    ('Gasolina', 'Gasolina'),
    ('Gas', 'Gas'),
    ('Diesel', 'Diesel'),
    ('Biodiesel', 'Biodiesel'),
]
class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=255,choices=COMBUSTIBLE_CHOICES,verbose_name="Tipo Combustible" )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')
    def __str__(self):
        return self.nombre
class ModeloAuto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Modelo")
    fabricante = models.ForeignKey("Fabricante",on_delete=models.SET_NULL, blank=True, null=True)
    tipo_combustible = models.ManyToManyField("TipoCombustible")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')
    def __str__(self):
        return self.nombre

