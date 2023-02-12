from .views import Registro, cerrars, log
from django.urls import path



urlpatterns = [

    path('', Registro.as_view(), name="Autenticacion"),  
    path('cerrars', cerrars, name="Cerrars"),
    path('log', log, name="Login"),
]
