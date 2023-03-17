from django.shortcuts import render,redirect
from AppContacto.forms import FormularioContacto


# Create your views here.
def contacto(request):
    formulario=FormularioContacto()#instancia formulario vacio para mostrar el form

    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)#si el metodo es post que creo un objeto formulario pasando los datos de la peticion por parametro
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")           

            return redirect("/contacto/?valido")

    return render(request, "AppContacto/contacto.html",{"miFormulario":formulario})
