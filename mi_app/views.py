# mi_app/views.py

from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

@login_required
def index(request):
    return render(request, 'plantilla/base.html')

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]  # Asegúrate de que el usuario esté autenticado

class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]  # Asegúrate de que el usuario esté autenticado
