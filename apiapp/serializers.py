#se encarga de hacer el crud desde json

from app.models import * 
from rest_framework import serializers 

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto 
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only = True)

    class Meta:
        model = Producto 
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class SuscriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscriptor
        fields = '__all__'
    
class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = '__all__'
