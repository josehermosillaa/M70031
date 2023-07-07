import datetime
from django.db import models

annos_choices = []

for r in range(1950, (datetime.datetime.now().year+1)):
    annos_choices.append((r, r))

def anno_actual():
    return datetime.date.today().year
# Create your models here.

class Fabricante(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre Fabricante")
    pais = models.CharField(max_length=255, default="Desconocido" ,verbose_name="Pais")
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
    f_fabricacion = models.IntegerField(choices=annos_choices, default=anno_actual, verbose_name='Fecha de Fabricacion')
    costo_fabricacion = models.DecimalField(null=False, decimal_places=2, max_digits=10, verbose_name="Costo de Fabricacion")
    tipo_combustible = models.ManyToManyField("TipoCombustible")
    precio_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10, verbose_name="Precio de Venta")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actuialización')
    def __str__(self):
        return self.nombre

