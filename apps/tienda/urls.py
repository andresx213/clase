from django.urls import path,include
from .views import intex
urlpatterns = [
    path('',intex),
]