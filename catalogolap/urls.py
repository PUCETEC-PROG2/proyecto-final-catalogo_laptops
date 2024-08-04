# Archivo: catalogolap/urls.py

from django.urls import path
from . import views  # Importa las vistas de la aplicación

urlpatterns = [
    path('', views.index, name='index'),  # Define la ruta para la vista 'index'
]
