from django.contrib import admin

#Importamos los modelos de la base de datos
# Register your models here.
from .models import Producto, Tienda, TiendaProducto


admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(TiendaProducto)

