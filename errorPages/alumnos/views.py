from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializers import AlumnoSerializer
from .forms import alumnoForm
from django.shortcuts import render

def agregar_alumno(request):
    form = alumnoForm
    return render(request, 'avila_oscar.html',{'form':form})

class AlumnoViewset(viewsets.ModelViewSet):
    #Conjunto de queries de la BD
    queryset = Alumno.objects.all()

    #Empaquetar y enviar la información
    serializer_class = AlumnoSerializer

    #Renderizar las respuestas
    renderer_classes = [JSONRenderer]