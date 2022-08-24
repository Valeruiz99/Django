from django.contrib import admin
from .models import Aprendiz, Monitorias, Actividades
from datetime import date

# Register your models here.

@admin.register(Aprendiz)#Ponemos el decorador para evitarnos la última línea de código, no ponemos admin.site.register(Aprendiz, AprendizAdmin)
class AprendizAdmin (admin.ModelAdmin):
    list_display = ('id','cedula', 'nombre', 'apellido','fecha_nacimiento', 'edad')#Este id es el que genera automáticamente Django
    search_fields = ('nombre','apellido','cedula')#Éste filtro de búsqueda es tipo "like" 
    
    def edad(self,obj):
        fechaHoy = date.today()
        edad = fechaHoy.year - obj.fecha_nacimiento.year - ((fechaHoy.month,fechaHoy.day)<(obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))
        return edad

#admin.site.register(Aprendiz, AprendizAdmin)#Le estoy diciendo que quiero crear un aprendiz, pero que quiero que se vean en la lista ciertos campos específicos que hago en la clase
@admin.register(Monitorias)
class MonitoriasAdmin (admin.ModelAdmin):
    list_display = ('id','cat', 'nombre','apellido','aprendiz','fechaInicio', 'fechaFinal',)
    search_fields = ('cat','aprendiz__nombre', 'aprendiz__apellido', 'aprendiz__cedula')#con el __ buscamos alguna propiedad del objeto aprendiz
    list_filter = ['cat', 'fechaInicio']
    list_editable = ['aprendiz']#Le ponemos el objeto y el único que se puede modificar es la llave foránea
    
    
    def apellido(self, obj):
        return obj.aprendiz.apellido#Campos virtuales que no existían y se pueden pintar en el list_display
    
    def nombre(self, obj):
        return obj.aprendiz.nombre

@admin.register(Actividades)
class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('id','monitoria', 'actividad', 'observaciones', 'fecha', )
    search_fields = ('monitoria','actividad')



