#corresponde a las url que se utilizaran 

from apiapp.views import ProductoViewSet
from rest_framework import routers
from django.urls import path ,include
from .views import * 

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('usuario',UsuarioViewSet)
router.register('carrito', CarritoViewSet)
router.register('suscriptor', SuscriptorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    


]