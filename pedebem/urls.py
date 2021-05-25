from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comandas', views.comandas, name='comandas'),
    path('a', views.teste, name ='teste'),
]