from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


app_name="carro"

urlpatterns= [
    
    path('Agregar/<int:producto_id>/', views.agregarP, name="agregar"), 
    path('Eliminar/<int:producto_id>/', views.eliminarP, name="eliminar"), 
    path('restar/<int:producto_id>/', views.restarP, name="restar"), 
    path('Limpiar/', views.limpiarC, name="limpiar"), 
    path('carros/', views.carro, name="Carros"),
]