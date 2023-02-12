from django.urls import path
from proyectoapp import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('recibos/', views.recibo, name="Recibos"), 
    path('carros/', views.carro, name="Carros"),  

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
