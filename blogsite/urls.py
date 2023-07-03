
from django.urls import path
# from .views import index
from . import views
urlpatterns = [

    path("", views.index, name='index'),
    path("add/", views.add, name='add'),
    path("add/addregister/", views.addregister, name='addregister'),
    path("delete/<int:id>/", views.delete, name='delete'),
    path("update/<int:id>/", views.update, name='update'),
    path("updateregister/<int:id>/", views.updateregister, name='update'),
]
