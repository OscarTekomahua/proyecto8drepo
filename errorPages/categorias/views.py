from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse
import json

# Create your views here.

def agregar_categorias(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = categoriaForm()

    return render(request, 'agregar_categoria.html', {'form':form})

def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje':'Registro exitoso',
                'id':categoria.id
            }, statu=201)
        except Exception as e:
            return JsonResponse({
                'Error':'Ocurrio un error inesperado:'+str(e)
            }, status=400)
    return JsonResponse({
        'Error':'Método no soportado'
    }, status=405)
    
def ver_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver_categoria.html', {'categorias':categorias})

def index(request):
    return render(request, 'categorias.html')

def lista_categorias(request):
    categorias = Categoria.objects.all()

    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]

    return JsonResponse(data, safe=False)
