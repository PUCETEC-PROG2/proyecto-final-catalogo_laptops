from django import forms
from .models import Cliente   # Importar modelo Cliente
from .models import Producto  # Importa el modelo Producto
from .models import Categoria


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'correo_electronico', 'direccion']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto  # Se especifica que el formulario se basa en el modelo Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']  # Se definen los campos que estarán en el formulario



# Formulario para el modelo Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion'] 