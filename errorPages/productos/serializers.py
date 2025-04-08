from rest_framework import serializers
from .models import Producto

#Un serializador es una clase que actúa sobre un modelo
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' #<------ Todos los campos