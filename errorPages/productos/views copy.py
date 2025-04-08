from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse


def agregar_producto(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = productoForm()
    
    return render(request,'agregar.html', {'form':form})

#Funcion que agregar producto desde una llamada asincrona
import json
#Etiqueta para evitar el uso de CSRF
#@csrf_exempt <----- evitar su uso a menos que estemos probando
def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #Funcion que toma texto crudo y lo convierte a JSON
            producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            ) #Nueva instancia de producto y automaticamente la inserta en la BD
            return JsonResponse({
                'mensaje':'Registro exitoso',
                'id': producto.id
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'Error':'Ocurrio un error inesperado:'+str(e)
            }, status=400)
    return JsonResponse({
        'Error':'Método no soportado'
    }, status = 405)

def ver_producto(request):
    #Obtener de la BD todos los productos
    productos = Producto.objects.all()
    return render(request, 'ver.html', {'productos':productos})

#Esta funcion carga los en el HTML los productos con JSON
def index(request):
    return render(request, 'productos.html')

def lista_productos(request):
    productos = Producto.objects.all()

    #Generar un diccionario al aire que ordene los productos
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)