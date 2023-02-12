from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns= [
    
    path("", views.procesarP, name="Procesar_Pedido") 

]