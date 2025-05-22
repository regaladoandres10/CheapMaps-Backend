from rest_framework import viewsets, filters
from django.db.models import Prefetch

#importar el modelo producto
from myapp.models import Producto, Tienda, TiendaProducto
#Importar el serializador del producto

from myapp.api.serializer import (
    ProductoSerializer,
    TiendaSerializer,
    TiendaProductoSerializer,
    ProductosDetallesSerializer
)

from django_filters.rest_framework import DjangoFilterBackend

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.prefetch_related(
        Prefetch('precios_tiendas', 
                queryset=TiendaProducto.objects.select_related('tienda_id'))
    )
    #Mecanismo de filtrado y ordenamiento
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]


    search_fields = ['nombre']
    #Le decimos que trabaje con todos los registros
    #queryset = Producto.objects.all()
    #Le decimos como serializar los datos
    ordering_fields = ['nombre', 'precios_tiendas__precio']  # Campos para ordenar
    ordering = ['nombre']  # Orden por defecto

    def get_serializer_class(self):
        return ProductosDetallesSerializer    
    

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.prefetch_related(
        Prefetch('productos_precios', 
                queryset=TiendaProducto.objects.select_related('producto_id'))
    )
    serializer_class = TiendaSerializer

class TiendaProductoViewSet(viewsets.ModelViewSet):
    queryset = TiendaProducto.objects.select_related('producto_id', 'tienda_id')
    serializer_class = TiendaProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'precio': ['gte', 'lte'],  #Permite filtrar por rango de precios
        'disponible': ['exact'],
        'producto_id': ['exact'],
        'tienda_id': ['exact']
    }
    ordering_fields = ['precio', 'producto_id__nombre']
    ordering = ['precio']  # Orden por defecto: precio más bajo primero