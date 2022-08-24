from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.IntegerField()
    fecha_nacimiento = models.DateField()#Si no quiero valores por defecto, hago la migración, y le doy 1, y le pongo una fecha por defecto temporal
    
    def __str__(self): #Si no ponemos esto, para devolver algo de la clase aprendiz
        return f"{self.nombre}"

class Monitorias(models.Model):
    cat = models.CharField(max_length=100)
    aprendiz = models.ForeignKey(Aprendiz, on_delete= models.DO_NOTHING)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    def __str__(self):
        return f"{self.aprendiz} - {self.cat}"#Este string, es el que me trae los valores solicitados
    #Y así, se llamarán en la tabla
    
class Actividades(models.Model):
    monitoria = models.ForeignKey(Monitorias, on_delete= models.DO_NOTHING)
    actividad = models.CharField(max_length=254)
    observaciones = models.TextField()
    fecha = models.DateField(auto_now_add= True)#El auto_now_add solo tiene valores True o False 
    def __str__(self):
        return self.actividad