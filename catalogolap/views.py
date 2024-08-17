from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

# Vista para la página principal
def index(request):
    return render(request, 'index.html')

# Vista para listar todos los clientes
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

# Vista para añadir un nuevo cliente
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('cliente_list')  # Redirige a la lista de clientes después de añadir uno nuevo
    else:
        form = ClienteForm()
    return render(request, 'cliente_edit.html', {'form': form})
