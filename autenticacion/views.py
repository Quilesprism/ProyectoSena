
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
class Registro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Inicio')
        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form":form})

def cerrars(request):
    logout(request)
    return redirect('Inicio')

def log(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            passs=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre, password=passs)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else: 
                messages.error(request, "usuario no valido")
        else: 
            messages.error(request, "Incorrecto")

    form=AuthenticationForm()
    return render(request, "login/login.html", {"form":form})
