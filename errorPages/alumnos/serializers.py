from rest_framework import serializers
from .models import Alumno

#Un serializador es una clase que actúa sobre un modelo
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__' #<------ Todos los campos