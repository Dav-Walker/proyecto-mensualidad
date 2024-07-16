from django.shortcuts import render, redirect
from django.contrib.auth.views import logout_then_login
from .forms import *

def home(request):
    return render(request, "core/index.html")

def cliente(request):
    return render(request, "core/cliente.html")

def gerente(request):
    return render(request, "core/gerente.html")

def gerente(request):
    return render(request, "core/loginregistro.html")

def logout(request):
    return logout_then_login(request, login_url="home")

def registro(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login') 
    else:
        registro = Registro()
    
    return render(request, 'core/registro.html',{'form':registro})