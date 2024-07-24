# mi_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "inicio"),
    path('salir/', views.salir, name= "salir")
]
