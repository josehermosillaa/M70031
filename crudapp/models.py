from django.db import models

# Create your models here.

class Empleado(models.Model):
    emp_id = models.CharField(max_length=3)
    emp_nombre = models.CharField(max_length=200)
    emp_correo = models.EmailField()
    emp_designacion = models.CharField(max_length=150)
    #buena practica
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        db_table="Employee"
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
