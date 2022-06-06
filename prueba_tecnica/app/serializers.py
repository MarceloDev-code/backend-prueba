from rest_framework import serializers
from .models import empresas, empleados

#Serializadores para empresas y empleados
class empresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresas
        fields = ('rut', 'nombre', 'direccion', 'telefono')
        
class empleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = ('rut', 'nombre', 'email', 'empresa')