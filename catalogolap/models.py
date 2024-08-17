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



# Create your models here.
