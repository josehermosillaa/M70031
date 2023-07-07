
from django.urls import path
# from .views import index
from . import views
urlpatterns = [

    path("", views.insertar_emp_view, name='insertar_emp'),
    path("mostrar/", views.mostrar_emp_view, name='mostrar_emp'),
    path("editar/", views.editar_emp_view, name='editar_emp'),
    path("eliminar/", views.eliminar_emp_view, name='eliminar_emp'),
]
