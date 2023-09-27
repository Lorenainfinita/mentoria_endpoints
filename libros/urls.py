from django.urls import path
from .views import ListaLibrosView, DetalleLibroView

urlpatterns = [
    path('libros/', ListaLibrosView.as_view(), name='lista-libros'),
    path('libros/<int:pk>/', DetalleLibroView.as_view(), name='detalle-libro'),
]
