# Archivo: catalogolap/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

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
