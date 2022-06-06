from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(empresas)
class empresasAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'direccion', 'telefono')
    list_filter = ('nombre',)
    search_fields = ('rut', 'nombre', 'direccion', 'telefono')
    ordering = ('nombre',)

@admin.register(empleados)
class empleadosAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'email', 'empresa')
    list_filter = ('nombre',)
    search_fields = ('rut', 'nombre', 'email', 'empresa')
    ordering = ('nombre',)