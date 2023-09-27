from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
        
###. Un serializador en Django REST Framework (DRF) es una herramienta esencial para convertir
# información de Python, especialmente objetos de modelos de Django, a formatos que puedan ser 
# enviados a través de la red, como JSON, y viceversa.