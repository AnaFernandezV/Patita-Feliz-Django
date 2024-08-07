from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('direccion/', direccion, name="direccion"),
    path('sub/', sub, name='sub'),
    path('producto/', producto, name='producto'),
    path('detalle-producto/', detalleproducto, name="detalleproducto"),
    path('iniciar-sesion/', iniciarsesion, name="iniciar-sesion"),  
    path('perfil/', perfil, name="perfil"),
    path('pedido/<id>', pedido, name="pedido"),
    path('seguimiento/', seguimiento, name="seguimiento"),

    #REGISTRAR, MODIFICAR, ELIMINAR Y LISTAR PRODUCTOS
    path('agregar_producto/', agregar_producto, name="agregar_producto"),     
    path('modificar_producto/<codigo>/', modificar_producto, name="modificar_producto"),
    path('eliminar/<codigo>/', eliminar_producto, name="eliminar_producto"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    
    #REGISTRAR, MODIFICAR, ELIMINAR Y LISTAR USUARIO
    path('registro/', registro, name="registro"),
    path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('eliminar_usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
    path('listar_usuario/', listar_usuario, name="listar_usuario"),

    #CARRITO 
    path('carrito/<id>/', carrito, name="carrito"),
    path('eliminar_carrito/<codigo>/', eliminar_carrito, name="eliminar_carrito"),

    #login
    path('accounts/',include('django.contrib.auth.urls')),

    #REGISTRO USUARIO
    path('registro_usuario', registro_usuario, name="registro_usuario"),
    
    #URL API 
    path('producto-api/', productoApi, name="producto-api"),
    path('rickandmorty/', apiRick , name="rickandmorty"),

]