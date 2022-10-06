"""pedebem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bar.views import ComandaDetailView, ComandaPagarView, index, ComandaListView
from bar import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('comandadetails', views.ComandaView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('comandas/', ComandaListView.as_view(), name='comandas'),
    path('comandas/<int:pk>', ComandaDetailView.as_view(), name='comandas_detail'),
    path('comandas/<int:pk>/fechar', ComandaPagarView.as_view(), name='comandas_fechar'),
    path('rest/', include(router.urls)),
]
