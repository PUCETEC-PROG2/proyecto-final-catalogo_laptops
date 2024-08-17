"""
URL configuration for proyecto_final_catalogo_laptops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Archivo: proyecto-final-catalogo_laptops/urls.py

from django.contrib import admin
from django.urls import path, include
from catalogolap import views  # Importa las vistas de la aplicación 'catalogolap'

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', views.index, name='index'),  # URL para la página de inicio que renderiza 'index.html'
    path('', include('catalogolap.urls')),  # Incluye las rutas de la aplicación 'catalogolap'
]
