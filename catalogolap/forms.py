from django import forms
from .models import Cliente, Producto, Categoria, Compra  # Importa también el modelo Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'correo_electronico', 'direccion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto  # Se especifica que el formulario se basa en el modelo Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']  # Se definen los campos que estarán en el formulario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

# Formulario para el modelo Compra
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra  # El modelo que se va a utilizar para el formulario
        fields = ['cliente', 'producto', 'categoria', 'cantidad']  # Excluye 'fecha_compra' porque no es editable

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()  # Poblamos el campo cliente con todos los clientes
        self.fields['producto'].queryset = Producto.objects.all()  # Poblamos el campo producto con todos los productos
        self.fields['categoria'].queryset = Categoria.objects.all()  # Poblamos el campo categoría con todas las categorías
