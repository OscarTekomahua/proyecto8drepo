from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewset
from .views import agregar_producto

#Definir un router
router = SimpleRouter()
router.register(r'api',ProductoViewset)

#ProductoViewset incluye: ip:8000/productos/api/ <-------- GET de todo
#ip:8000/productos/api/{id} <-------- GET, POST, PUT, DELETE de uno

urlpatterns = [
    path('', include(router.urls)),
    path('agregar_producto/', agregar_producto, name="agregar")
]