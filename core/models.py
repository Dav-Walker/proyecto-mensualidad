from django.db import models
from django.core.validators import MaxValueValidator

class datos_abuelos(models.Model):
    name =models.CharField(max_length=50)
    edad = models.IntegerField(default=65, validators=[MaxValueValidator(110)])
    fecha_inicio_cont =models.DateField()
    fecha_paga =models.DateField()
    monto_pagado = models.IntegerField()
    cant_pag_atrasados = models.IntegerField()
    monto_atrasado = models.IntegerField()
    class Meta:
        db_table ='datos_abuelos'