from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewset
from .views import agregar_alumno

#Definir un router
router = SimpleRouter()
router.register(r'api',AlumnoViewset)

#ProductoViewset incluye: ip:8000/productos/api/ <-------- GET de todo
#ip:8000/productos/api/{id} <-------- GET, POST, PUT, DELETE de uno

urlpatterns = [
    path('', include(router.urls)),
    path('registrar_alumno/', agregar_alumno, name='add_alumn0')
]