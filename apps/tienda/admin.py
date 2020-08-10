from django.contrib import admin
from apps.tienda.models import cuotas, cliente

# Register your models here.
admin.site.register(cuotas)
admin.site.register(cliente)