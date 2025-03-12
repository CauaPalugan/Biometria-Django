from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from biometria_app import views

urlpatterns = [
    path('', views.firstLogin, name='firstLogin'),
    path('cadastro', views.cadastro, name='cadastro'),
]
