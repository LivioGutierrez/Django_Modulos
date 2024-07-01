from django.shortcuts import render,HttpResponse
from .models import Pelicula, Cliente

# Create your views here.
def index(request):
    #select * from peliculas;
    peliculas = Pelicula.objects.all()
    print(peliculas)
    
    #select * from peliculas WHERE Shueck;
    pelicula_shueck = Pelicula.objects.filter(titulo= 'Shueck')
    print(pelicula_shueck)
    
    return HttpResponse("Ejecucion correcta")

def cliente(request): #Mostrar html
    lista_clientes = Cliente.objects.all()
    
    return render(request,"cliente.html",{'lista_clientes':lista_clientes})

def crear_cliente(request): #Guarda en la base de datos
    pass

def editar_cliente(request):#Mostrar html
    pass

def actualizar_cliente(request):
    pass

def eliminar_cliente(request):
    pass