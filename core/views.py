from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

def cliente(request):
    return render(request, "core/cliente.html")

def gerente(request):
    return render(request, "core/gerente.html")

def gerente(request):
    return render(request, "core/loginregistro.html")