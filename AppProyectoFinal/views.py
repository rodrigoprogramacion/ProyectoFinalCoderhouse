from django.shortcuts import render,HttpResponse
from AppCarro.carro import Carro



# Create your views here.
def home(request):
    carro=Carro(request)
    return render(request,"AppProyectoFinal/home.html")


def quienesSomos(request):
    return render(request, "AppProyectoFinal/quienesSomos.html")