from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from pedidos.models import LineaPedido, Pedido
from carrito.carro import Carro
from django.contrib import messages
from flask import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


@login_required(login_url="/autenticacion/logear")
def procesarP(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request) # Se coge el carro
    pdi = list() #Lista en la que iran los elementos que tiene un pedido del carro
    for key, value in carro.carro.items(): #for que recorre los productos del carro
        pdi.append(LineaPedido(  
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
            ))

    LineaPedido.objects.bulk_create(pdi) #crea registros en la base de datos

    enviar_mail( 
        pedido=pedido, 
        pdi=pdi, 
        nombreusuraio=request.user.username,
        emailusuario=request.user.email

    )
       
    #mensaje de fin
    messages.success(request, "El pedido se ha creado")

    return redirect('../tienda/tienda')


def enviar_mail(**kwargs):
    asunto = "Pedido realizado"
    mensaje= render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "pdi": kwargs.get("pdi"),
        "nombreusuario": kwargs.get("nombreusuario")

        })

    mensajeT=strip_tags(mensaje)
    fromemail="quilesxasterin8@gmail.com"
    to=kwargs.get("emailusuario")
    #to="qagonzalezr@correo.udistrital.edu.co"
    send_mail(asunto, mensajeT, fromemail, [to], html_message=mensaje)