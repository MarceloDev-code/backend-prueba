from django.db import models

# Create your models here.

class empresas(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, unique=True, null=False, blank=False, verbose_name='Rut')
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    direccion = models.CharField(max_length=100, null=False, blank=False, verbose_name='Dirección')
    telefono = models.CharField(max_length=20, null=False, blank=False, verbose_name='Teléfono')
    
    def __str__(self):
        return self.nombre
    
class empleados(models.Model):
    rut = models.CharField(max_length=10, primary_key=True, unique=True, null=False, blank=False, verbose_name='Rut')
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nombre')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Email')
    empresa = models.ForeignKey(empresas, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Empresa')
