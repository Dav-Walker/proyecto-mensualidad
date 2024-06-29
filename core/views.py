from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def cliente(request):
    return render(request, "cliente.html")

def gerente(request):
    return render(request, "gerente.html")