from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('clientes/', views.cliente_list, name='cliente_list'),  # URL para la lista de clientes
    path('clientes/nuevo/', views.cliente_new, name='cliente_new'),  # URL para añadir un nuevo cliente
    path('clientes/<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),  # Editar cliente existente
    path('productos/', views.product_list, name='producto_list'),  # URL para la lista de productos
    path('productos/nuevo/', views.producto_new, name='producto_new'), 
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),  # URL para eliminar productos # URL para añadir un nuevo producto
    path('categorias/', views.categoria_list, name='categoria_list'),  # URL para la lista de categorías
    path('categorias/nuevo/', views.categoria_new, name='categoria_new'),  # URL para añadir una nueva categoría
    path('categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),  # URL para editar una categoría existente
    path('compras/', views.compra_list, name='compra_list'),  # URL para la lista de compras
    path('compras/nuevo/', views.compra_new, name='compra_new'),  # URL para añadir una nueva compra
    path('compras/<int:pk>/editar/', views.compra_edit, name='compra_edit'),  # Editar compra existente
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
