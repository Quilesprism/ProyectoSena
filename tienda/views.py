
from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from .models import Producto, CategoriaP
#from tienda.models import 
# Create your views here.


def tienda(request):
    productos=Producto.objects.all()
    
    return render(request, "tienda/tienda.html", {"productos": productos})

#def carro(request):
#    return render(request, "carro/widget.html")