from django.contrib import admin
from.models import *

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','precioNormal','precioSub','stock','tipo', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 10

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['run','nombre','apellido','correo','contrasena']
    search_fields = ['run']
    list_per_page = 10

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'precio', 'imagen']
    search_fields = ['codigo']
    list_per_page = 10


admin.site.register(TipoProducto)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Carrito,CarritoAdmin)

