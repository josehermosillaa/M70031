from django.db import models

# Create your models here.

CHOICE_FIELDS=[
    ('Project Manager','Project Manager'),
    ('Programador','Programador'),
    ('Soporte Técnico','Soporte Técnico'),
    ('Desarrollador Web','Desarrollador Web'),
]
class Empleado(models.Model):
    emp_id = models.CharField(max_length=3, verbose_name='Id')
    emp_nombre = models.CharField(max_length=200, verbose_name='Nombre')
    emp_correo = models.EmailField(verbose_name='Email')
    emp_designacion = models.CharField(max_length=150, choices=CHOICE_FIELDS,verbose_name='Designación')
    #buena practica
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        db_table="Employee"
        verbose_name='Empleado'
        verbose_name_plural='Empleados'

    def __str__(self):
        return self.emp_nombre + " " + self.emp_designacion
    