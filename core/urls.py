from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',home, name='home'),
    path('cliente/',cliente, name='cliente'),
    path('gerente/',gerente, name='gerente'),
    path('loginregistro/',gerente, name='login'),
    path('login',LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout',logout, name='logout'),
    path('registro',registro, name='registro'),
]