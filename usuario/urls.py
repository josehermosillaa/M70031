
from django.urls import path
# from .views import index
from . import views
urlpatterns = [
    path("registro/", views.registro_views, name='registro'),
]
