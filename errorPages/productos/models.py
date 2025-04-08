from django.db import models
from categorias.models import Categoria

class Producto(models.Model):
    #Aquí van los atributos
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #Los campos URLFields limitan los campos a 200 caracteres por defecto
    imagen = models.URLField()

    #Agregar una relación con categorias
    #Parametros: modelo, 
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre