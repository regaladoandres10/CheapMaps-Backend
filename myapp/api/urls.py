from rest_framework.routers import DefaultRouter
from myapp.api.views import ProductoViewSet, TiendaViewSet, TiendaProductoViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet, basename='producto')
router.register('tiendas', TiendaViewSet, basename='tienda')
router.register('tiendaproducto', TiendaProductoViewSet)
urlpatterns = router.urls