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
    list_display = ['codigo', 'nombre', 'precio','precioSub', 'imagen']
    search_fields = ['codigo']
    list_per_page = 10

class SusAdmin(admin.ModelAdmin):
    list_display = ['email','sub']
    search_fields = ['email']
    list_per_page = 10

class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['cantidad','usuario','estado']
    search_fields = ['codigo']
    list_per_page = 10

admin.site.register(TipoProducto)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Suscriptor,SusAdmin)
admin.site.register(Seguimiento,SeguimientoAdmin)
