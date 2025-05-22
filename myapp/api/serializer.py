from rest_framework import serializers
from myapp.models import Producto, Tienda,  TiendaProducto

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ['id', 'nombre', 'direccion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        #fields = '__all__'
        fields = ['id', 'nombre', 'descripcion', 'imagen_url']

class TiendaProductoSerializer(serializers.ModelSerializer):
    tienda = TiendaSerializer(read_only=True, source='tienda_id')
    #producto_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TiendaProducto
        fields = ['id', 'producto_id', 'tienda', 'precio', 'disponible']


class ProductosDetallesSerializer(serializers.ModelSerializer):

    precios = TiendaProductoSerializer(
            many = True,
            source='precios_tiendas',
            read_only = True,
        )
        
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'imagen_url', 'precios']
        
