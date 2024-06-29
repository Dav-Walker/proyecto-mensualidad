from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('cliente/',cliente, name='cliente'),
    path('gerente/',gerente, name='gerente')

]