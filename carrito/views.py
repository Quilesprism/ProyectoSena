from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect



def agregarP(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")

def eliminarP(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restarP(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("Tienda")

def limpiarC(request, producto_id):
    carro=Carro(request)
    carro.limpiar()
    return redirect("Tienda")