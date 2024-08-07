from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('clientes/', views.cliente_list, name='cliente_list'),  # URL para la lista de clientes
    path('clientes/nuevo/', views.cliente_new, name='cliente_new'),  # URL para añadir un nuevo cliente
    path('clientes/<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),  # Editar cliente existente
    path('productos/', views.product_list, name='producto_list'),  # URL para la lista de productos
    path('productos/nuevo/', views.producto_new, name='producto_new'),  # URL para añadir un nuevo producto
    path('categorias/', views.categoria_list, name='categoria_list'),  # URL para la lista de categorías
    path('categorias/nuevo/', views.categoria_new, name='categoria_new'),  # URL para añadir una nueva categoría
    path('categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),  # URL para editar una categoría existente
    # Aquí puedes añadir las demás rutas para productos, categorías, etc.
]
