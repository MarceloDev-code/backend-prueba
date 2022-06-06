from django.urls import re_path
from app import views

urlpatterns = [
    re_path(r'^api/empresas$', views.empresas_list),
    re_path(r'^api/empresas/(?P<pk>[0-9]{8}[0-9kK]{1}$)$', views.empresas_detail),
    re_path(r'^api/empleados$', views.empleados_create),
    re_path(r'^api/empleados/(?P<pk>[0-9]{8}[0-9kK]{1}$)$', views.empleados_list),
    
    
]

