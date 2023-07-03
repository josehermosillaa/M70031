
from django.urls import path
# from .views import index
from . import views
urlpatterns = [

    path("", views.index, name='index'),
    path("add/", views.add, name='add'),
    path("add/addregister/", views.addregister, name='addregister'),
]
