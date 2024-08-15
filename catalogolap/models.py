from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)  # ID del cliente, clave primaria
    nombre = models.CharField(max_length=100)  # Nombre del cliente
    apellido = models.CharField(max_length=100)  # Apellido del cliente
    cedula = models.CharField(max_length=20, unique=True)  # Cédula de identificación, única
    correo_electronico = models.EmailField()  # Correo electrónico del cliente
    direccion = models.CharField(max_length=255)  # Dirección del cliente

    class Meta:
        db_table = 'cliente'  # Indica que la tabla se llama 'cliente'
        managed = False  # Django no gestionará la creación ni eliminación de esta tabla


    def __str__(self):
        return f'{self.nombre} {self.apellido}'  # Representación del cliente





# Modelo para representar los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Campo para el nombre del producto
    descripcion = models.TextField()  # Campo para la descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el precio del producto
    stock = models.IntegerField()  # Campo para la cantidad en stock del producto

    def __str__(self):
        return self.nombre  # Método para representar el objeto Producto como una cadena
# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la categoría

    def __str__(self):
        return self.nombre  # Retorna el nombre de la categoría como representación en string
    

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)  # Incluye este campo para la descripción

    def __str__(self):
        return self.nombre
    

class Compra(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)  # Relación con Cliente
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)  # Relación con Producto
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)  # Relación con Categoria
    cantidad = models.PositiveIntegerField()  # Cantidad de productos comprados
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la compra
    fecha_compra = models.DateTimeField(auto_now_add=True)  # Fecha de la compra

    def __str__(self):
        return f'Compra de {self.cantidad} {self.producto.nombre} por {self.cliente.nombre}'
    

