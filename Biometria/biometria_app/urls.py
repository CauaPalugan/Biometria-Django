from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstLogin, name='firstLogin'),
    path('cadastro', views.cadastro, name='cadastro'),
]