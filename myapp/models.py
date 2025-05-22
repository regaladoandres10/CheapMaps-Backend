from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen_url = models.URLField()

    #Hacer que tenga formato en la vista del admin-site
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        #Cambiando el nombre de la tabla
        db_table = "Producto"

    

class Tienda(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"
        db_table = "Tienda"

#Relación de muchos a muchos
class TiendaProducto(models.Model):
    producto_id = models.ForeignKey(
            Producto, 
            on_delete=models.CASCADE,
            related_name='precios_tiendas'  # Nombre más descriptivo
    )
    tienda_id = models.ForeignKey(
        Tienda, 
        on_delete=models.CASCADE,
        related_name='productos_precios'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.producto_id.nombre + " - " + self.tienda_id.nombre

    class Meta:
        verbose_name = "TiendaProducto"
        verbose_name_plural = "TiendasProductos"
        db_table = "TiendaProducto"
        #Claves unicas
        #unique_together = [['producto', 'tienda']]