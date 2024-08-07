# Archivo: catalogolap/views.py

# Archivo: catalogolap/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto, Categoria, Compra  # Importa los modelos necesarios, incluyendo Compra
from .forms import ClienteForm, ProductoForm, CategoriaForm, CompraForm  # Importa los formularios necesarios

# Vista para la página principal
def index(request):
    return render(request, 'index.html')

# Vista para listar todos los clientes
def cliente_list(request):
    clientes = Cliente.objects.all()  # Obtiene todos los clientes de la base de datos
    return render(request, 'cliente_list.html', {'clientes': clientes})

# Vista para añadir un nuevo cliente
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)  # Procesa el formulario si se envió mediante POST
        if form.is_valid():
            cliente = form.save(commit=False)  # Guarda el formulario pero no lo envía aún a la base de datos
            cliente.save()  # Guarda el cliente en la base de datos
            return redirect('cliente_list')  # Redirige a la lista de clientes después de añadir uno nuevo
    else:
        form = ClienteForm()  # Si es un GET, muestra un formulario vacío
    return render(request, 'cliente_edit.html', {'form': form})

# Vista para editar un cliente existente
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)  # Obtiene el cliente por su clave primaria (pk) o muestra un error 404 si no se encuentra
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)  # Pasa el formulario con los datos existentes del cliente
        if form.is_valid():
            form.save()  # Guarda los cambios del formulario
            return redirect('cliente_list')  # Redirige a la lista de clientes después de editar
    else:
        form = ClienteForm(instance=cliente)  # Carga el formulario con los datos actuales del cliente
    return render(request, 'cliente_edit.html', {'form': form})  # Renderiza el formulario de edición

# Vista para listar todos los productos
def product_list(request):
    productos = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'product_list.html', {'productos': productos})  # Renderiza la plantilla `product_list.html` con los productos

# Vista para añadir un nuevo producto
def producto_new(request):
    if request.method == "POST":  # Si el formulario se envía con un método POST
        form = ProductoForm(request.POST)  # Se crea una instancia del formulario con los datos del POST
        if form.is_valid():  # Se valida el formulario
            producto = form.save(commit=False)  # Se guarda el producto, pero no se guarda en la base de datos aún
            producto.save()  # Se guarda el producto en la base de datos
            return redirect('producto_list')  # Redirige a la lista de productos después de añadir uno nuevo
    else:
        form = ProductoForm()  # Si no es un método POST, se crea un formulario vacío
    return render(request, 'producto_edit.html', {'form': form})  # Renderiza el formulario en la plantilla `producto_edit.html`

# Vista para listar todas las categorías
def categoria_list(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías de la base de datos
    return render(request, 'categoria_list.html', {'categorias': categorias})  # Renderiza la plantilla `categoria_list.html` con las categorías

# Vista para añadir una nueva categoría
def categoria_new(request):
    if request.method == "POST":  # Si el formulario se envía con un método POST
        form = CategoriaForm(request.POST)  # Se crea una instancia del formulario con los datos del POST
        if form.is_valid():  # Se valida el formulario
            categoria = form.save(commit=False)  # Se guarda la categoría, pero no se guarda en la base de datos aún
            categoria.save()  # Se guarda la categoría en la base de datos
            return redirect('categoria_list')  # Redirige a la lista de categorías después de añadir una nueva
    else:
        form = CategoriaForm()  # Si no es un método POST, se crea un formulario vacío
    return render(request, 'categoria_edit.html', {'form': form})  # Renderiza el formulario en la plantilla `categoria_edit.html`

# Vista para editar una categoría existente
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)  # Obtiene la categoría por su clave primaria (pk) o muestra un error 404 si no se encuentra
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)  # Pasa el formulario con los datos existentes de la categoría
        if form.is_valid():
            form.save()  # Guarda los cambios del formulario
            return redirect('categoria_list')  # Redirige a la lista de categorías después de editar
    else:
        form = CategoriaForm(instance=categoria)  # Carga el formulario con los datos actuales de la categoría
    return render(request, 'categoria_edit.html', {'form': form})  # Renderiza el formulario de edición

# Vista para listar todas las compras
def compra_list(request):
    compras = Compra.objects.all()  # Obtiene todas las compras de la base de datos
    return render(request, 'compra_list.html', {'compras': compras})  # Renderiza la plantilla `compra_list.html` con las compras

# Vista para añadir una nueva compra
def compra_new(request):
    if request.method == "POST":  # Si el formulario se envía con un método POST
        form = CompraForm(request.POST)  # Se crea una instancia del formulario con los datos del POST
        if form.is_valid():  # Se valida el formulario
            compra = form.save(commit=False)  # Se guarda la compra, pero no se guarda en la base de datos aún
            compra.save()  # Se guarda la compra en la base de datos
            return redirect('compra_list')  # Redirige a la lista de compras después de añadir una nueva
    else:
        form = CompraForm()  # Si no es un método POST, se crea un formulario vacío
    return render(request, 'compra_edit.html', {'form': form})  # Renderiza el formulario en la plantilla `compra_edit.html`

# Vista para editar una compra existente
def compra_edit(request, pk):
    compra = get_object_or_404(Compra, pk=pk)  # Obtiene la compra por su clave primaria (pk) o muestra un error 404 si no se encuentra
    if request.method == "POST":
        form = CompraForm(request.POST, instance=compra)  # Pasa el formulario con los datos existentes de la compra
        if form.is_valid():
            form.save()  # Guarda los cambios del formulario
            return redirect('compra_list')  # Redirige a la lista de compras después de editar
    else:
        form = CompraForm(instance=compra)  # Carga el formulario con los datos actuales de la compra
    return render(request, 'compra_edit.html', {'form': form})  # Renderiza el formulario de edición
