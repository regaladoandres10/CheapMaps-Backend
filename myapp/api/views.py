from rest_framework import viewsets
#importar el modelo producto
from myapp.models import Producto
#Importar el serializador del producto
from myapp.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    #Le decimos que trabaje con todos los registros
    queryset = Producto.objects.all()
    #Le decimos como serializar los datos
    serializer_class = ProductoSerializer