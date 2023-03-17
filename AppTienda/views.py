from django.shortcuts import render
from .models import Producto
# Create your views here.


def tienda(request):

    productos=Producto.objects.all() #guardamos en una variable todos los productos de la base  de datos

    return render(request,"AppTienda/tienda.html",{"productos":productos})