from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('clientes/', views.cliente_list, name='cliente_list'),  # URL para la lista de clientes
    path('clientes/nuevo/', views.cliente_new, name='cliente_new'),  # URL para añadir un nuevo cliente
    path('clientes/<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),  # Editar cliente existente
    # Aquí puedes añadir las demás rutas para productos, categorías, etc.
]
