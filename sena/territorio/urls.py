from unicodedata import name
from django.urls import path
from . import views


#El urlpatterns es un vector
app_name = "territorio"#Namespace, es la ruta base
urlpatterns = [
    path('', views.index, name='index'),
    path('aprendiz/', views.listarAprendiz, name='aprendiz'),
    path('aprendiz-add/', views.insertarAprendiz, name='aprendiz-add'),
    path('aprendiz-guardar/', views.guardarAprendiz, name='aprendiz-guardar'),
    path('aprendiz-eliminar/<int:id>', views.eliminarAprendiz, name='aprendiz-eliminar'),
    path('aprendiz-editar/<int:id>', views.editarAprendiz, name='aprendiz-editar'),
    path('aprendiz-actualizar/', views.actualizarAprendiz, name='aprendiz-actualizar'),
    
    
    path('monitorias/', views.listarMonitorias, name='monitorias'),
    path('monitorias-add/', views.insertarMonitoria, name='monitorias-add'),
    path('monitorias-guardar/', views.guardarMonitoria, name='monitorias-guardar'),
    
    
    path('actividades/', views.listarActividades, name='actividades'),
    path('actividades-add/', views.insertarActividad, name='actividades-add'),
    path('actividades-guardar/', views.guardarActividad, name='actividades-guardar'),
    
]

