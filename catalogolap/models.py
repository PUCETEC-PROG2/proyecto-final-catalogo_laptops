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
