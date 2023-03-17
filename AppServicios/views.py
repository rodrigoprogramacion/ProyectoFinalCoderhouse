from django.shortcuts import render
from AppServicios.models import Servicio
# Create your views here.


def servicios(request):

    servicios=Servicio.objects.all()  #crea on objeto de todos los servicios que haya en la base de datos
    return render(request,"AppServicios/servicios.html" , {"servicios":servicios})