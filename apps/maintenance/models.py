from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    numero_cc = models.IntegerField()
    fecha = models.DateField()

