from rest_framework import viewsets, filters
#importar el modelo producto
from myapp.models import Producto
#Importar el serializador del producto
from myapp.api.serializer import ProductoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductoViewSet(viewsets.ModelViewSet):
    #Le decimos que trabaje con todos los registros
    queryset = Producto.objects.all()
    #Le decimos como serializar los datos
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    #Ordemaos por el precio mas bajo al más alto
    filterset_fields = ['precio']
    ordering_fields = ['precio']
    ordering = ['precio']