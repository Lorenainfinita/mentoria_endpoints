from django.shortcuts import render
from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer

class ListaLibrosView(generics.ListCreateAPIView): ###generics.ListCreateAPIView. vista genérica 
    ##proporcionada por DRF para listar (get) y crear objetos (post).
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class DetalleLibroView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
###Entonces, ListaLibrosView maneja tanto la operación de listar (mediante GET) como la operación 
# de crear (mediante POST). Es una vista genérica 
# proporcionada por Django REST Framework que simplifica la implementación de estos endpoints.


###Esta vista está diseñada para manejar operaciones específicas para un libro individual en tu API.
'''Operaciones:
Recuperar detalles de un libro (método GET)
Devuelve información detallada sobre un libro específico.
Actualizar un libro (método PUT o PATCH)
Permite modificar la información de un libro existente.
Eliminar un libro (método DELETE)
Permite eliminar un libro existente.'''