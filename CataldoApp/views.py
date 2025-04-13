from django.shortcuts import render, redirect
from django.http import HttpResponse
from CataldoApp.forms import CreacionSocio 
from CataldoApp.models import Socio

# Create your views here.
def home(request):
    return render(request, 'home/home.html') 

def crear_socio(request):
    if request.method == 'POST':
        formulario = CreacionSocio(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            socio = Socio(nombre=info.get('nombre'), apellido=info.get('apellido'), dni=info.get('dni'), direccion=info.get('direccion'), celular=info.get('celular'))
            socio.save()
            return redirect('listado_de_socios')
    else:
        formulario = CreacionSocio()    
     
    return render(request, 'home/crear_socio.html', {'formulario': formulario})

def listado_de_socios(request):
    consulta = request.GET.get("q")
    if consulta:
        socios = Socio.objects.filter(apellido__icontains=consulta)
    else:
        socios = Socio.objects.all()
    return render(request, 'home/listado_de_socios.html', {'socios': socios})