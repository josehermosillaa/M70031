from django.contrib import admin
from .models import ModeloAuto, Fabricante, TipoCombustible, DirectorEjecutivo

# Register your models here.
my_models = [ModeloAuto, Fabricante, TipoCombustible, DirectorEjecutivo]
admin.site.register(my_models)
# admin.site.register(ModeloAuto)
# admin.site.register(TipoCombustible)