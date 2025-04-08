from django.urls import path
from .views import *

urlpatterns = [
    path('registrar/', agregar_categorias, name='registrar'),
    path('api/get', ver_categoria, name='ver'),
    path('', index, name='home_categoria'),
    path('json/', lista_categorias, name='lista_categorias'),
    path('api/post/', registrar_categoria, name='post')
]