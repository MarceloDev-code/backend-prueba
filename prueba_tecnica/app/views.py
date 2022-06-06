from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import empresasSerializer, empleadosSerializer
from .models import empresas, empleados
# Create your views here.
@api_view(['GET', 'POST'])
def empresas_list(request):
    if request.method == 'GET':
        empresas_listado = empresas.objects.all()
        
        rut = request.GET.get('rut', None)
        if rut is not None:
            empresas_listado = empresas_listado.filter(rut__icontains=rut)
        
        empresas_serializer = empresasSerializer(empresas_listado, many=True)
        return JsonResponse(empresas_serializer.data, safe=False)
    elif request.method == 'POST':
        empresas_data = JSONParser().parse(request)
        empresas_serializer = empresasSerializer(data=empresas_data)
        if empresas_serializer.is_valid():
            empresas_serializer.save()
            return JsonResponse(empresas_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(empresas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
def empresas_detail(request, pk):
    empresas_listado = empresas.objects.get(rut=pk)
    if request.method == 'GET': 
        empresas_serializer = empresasSerializer(empresas_listado) 
        return JsonResponse(empresas_serializer.data) 
    

@api_view(['GET'])
def empleados_list(request,pk):
    if request.method == 'GET':
        empleados_listado = empleados.objects.all()
        
        empresa_empleado = request.GET.get('empresa', None)
        if empresa_empleado is not None:
            empleados_listado = empleados_listado.filter(empresa__icontains=empresa_empleado)
        
        empleados_serializer = empleadosSerializer(empleados_listado, many=True)
        return JsonResponse(empleados_serializer.data, safe=False)
    
    
@api_view(['POST'])
def empleados_create(request):
    empleados_data = JSONParser().parse(request)
    empleados_serializer = empleadosSerializer(data=empleados_data)
    if empleados_serializer.is_valid():
        empleados_serializer.save()
        return JsonResponse(empleados_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(empleados_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def empleados_detail(request, pk):
    empleados = empleados.objects.get(rut=pk)
    if request.method == 'GET': 
        empleados_serializer = empleadosSerializer(empleados) 
        return JsonResponse(empleados_serializer.data) 