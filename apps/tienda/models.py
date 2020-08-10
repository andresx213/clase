from django.db import models
from apps.maintenance.models import cliente
# Create your models here.
class cuotas(models.Model):
    pricio = models.IntegerField()


class tienda(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono= models.CharField(max_length=12)
    edad = models.IntegerField()
    email = models.EmailField()
    cliente = models.ForeignKey(cliente, null=True,blank=True, on_delete=models.CASCADE)
    cuotas = models.ManyToManyField(cuotas)