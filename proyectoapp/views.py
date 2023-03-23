from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from carrito.carro import Carro
from servicios.models import Servicio
def home(request): 
    return render(request, "proyectoapp/index.html")


def recibo(request): 
    return render(request, "proyectoapp/recibo.html")

def carro(request):
    return render(request, "carro/widget.html")


