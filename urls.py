from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prueba/', views.formulario, name='formulario'),
    path('guardar_incidencia/', views.guardar_incidencia, name='guardar_incidencia'),
    path('obtener_incidencias/', views.obtener_incidencias, name='obtener_incidencias'),
    path('eliminar_incidencia/', views.eliminar_incidencia, name='eliminar_incidencia'),
    path('editar_incidencia/', views.editar_incidencia, name='editar_incidencia'),
]