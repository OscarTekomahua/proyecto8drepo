from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Producto
from .serializers import ProductoSerializer
from .forms import productoForm

def agregar_producto(request):
        form = productoForm()
        return render(request, 'agregar.html',{'form':form},status=200)

class ProductoViewset(viewsets.ModelViewSet):
    #Conjunto de queries de la BD
    queryset = Producto.objects.all()

    #Empaquetar y enviar la información
    serializer_class = ProductoSerializer

    #Renderizar las respuestas
    renderer_classes = [JSONRenderer]

    