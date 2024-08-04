# Archivo: catalogolap/views.py

from django.shortcuts import render  # Importa la función 'render' para renderizar plantillas

def index(request):
    # Renderiza la plantilla 'index.html' desde el directorio 'templates'
    return render(request, 'index.html')

# Create your views here.
