
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto, Categoria, Compra
from .forms import ClienteForm, ProductoForm, CategoriaForm, CompraForm
from django.contrib.auth.decorators import login_required

# Vista para la página principal
def index(request):
    return render(request, 'index.html')

# Vista para listar todos los clientes
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

# Vista para añadir un nuevo cliente
@login_required
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_edit.html', {'form': form})

# Vista para editar un cliente existente
@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_edit.html', {'form': form})

# Vista para listar todos los productos
@login_required
def product_list(request):
    productos = Producto.objects.all()
    return render(request, 'product_list.html', {'productos': productos})

# Vista para añadir un nuevo producto
@login_required
def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'producto_edit.html', {'form': form})

# Vista para listar todas las categorías
@login_required
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})

# Vista para añadir una nueva categoría
@login_required
def categoria_new(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_edit.html', {'form': form})

# Vista para editar una categoría existente
@login_required
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria_edit.html', {'form': form})

# Vista para listar todas las compras
@login_required
def compra_list(request):
    compras = Compra.objects.all()
    return render(request, 'compra_list.html', {'compras': compras})

# Vista para añadir una nueva compra
@login_required
def compra_new(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.save()
            return redirect('compra_list')
    else:
        form = CompraForm()
    return render(request, 'compra_edit.html', {'form': form})

# Vista para editar una compra existente
@login_required
def compra_edit(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'compra_edit.html', {'form': form})

@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})