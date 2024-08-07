from xmlrpc.client import Boolean
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)
    nombre = models.CharField(max_length=100)
    precioNormal = models.IntegerField()
    precioSub = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos",null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    run = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.CharField(max_length=50) 
    contrasena = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)  
   
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)    
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    precioSub= models.IntegerField()
    cantidad = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos_carrito",null=True)
    usuario = models.IntegerField(default=0)
    
    def __str__(self):
        return self.codigo

class Suscriptor(models.Model):
    email = models.EmailField(null=False,primary_key=True)
    sub = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sub

class EstadoPedido(models.Model):
    estado = models.CharField(max_length=60)

    def __str__(self):
        return self.estado

class Seguimiento(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)    
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    precioSub= models.IntegerField()
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="productos_carrito",null=True)
    usuario = models.IntegerField(default=0)

    def __str__(self):
        return self.codigo