from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('proveedor/', views.registrar_proveedor, name='proveedor'),
    path('logout', views.cerrar_sesion, name='cerrar sesion')
]