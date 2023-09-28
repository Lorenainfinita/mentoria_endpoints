from django.urls import path
from .views import ListaLibrosView, DetalleLibroView

urlpatterns = [
    path('libros/', ListaLibrosView.as_view(), name='lista-libros'),
    ####Cuando un usuario acceda a 'libros/' en su navegador, se ejecutará ListaLibrosView
    ###name='lista-libros' es un nombre simbólico para esta ruta, que puedes
    #utilizar para referenciarla en otras partes de tu aplicación.
    path('libros/<int:pk>/', DetalleLibroView.as_view(), name='detalle-libro'),
    ####Esta ruta utiliza <int:pk> para capturar la clave primaria del libro y está asociada 
    # a la vista DetalleLibroView, que es responsable de mostrar los detalles de ese libro específico.
]
