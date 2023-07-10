from django.contrib import admin
from .models import ModeloAuto, Fabricante, TipoCombustible, DirectorEjecutivo

# Register your models here.
class FabricanteAdmin(admin.ModelAdmin):
    search_fields = ('nombre','pais')
    fields = ['nombre', 'pais']
    list_display = ('id', 'nombre', 'pais')
    list_display_links = ['nombre']
    ordering = ('nombre', 'pais')

class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','fabricante','f_fabricacion','costo_fabricacion','precio_venta', 'costo')
    ordering=('fabricante','nombre')
    list_display_links = ['nombre', 'fabricante']
    list_filter = ('nombre', 'fabricante')
    list_per_page=6

    def costo(self, obj):
        return 'Costo Alto' if obj.precio_venta>5000 else 'Costo Bajo'

my_models = [TipoCombustible, DirectorEjecutivo]
admin.site.register(ModeloAuto, ModeloAutoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(my_models)
# admin.site.register(ModeloAuto)
# admin.site.register(TipoCombustible)