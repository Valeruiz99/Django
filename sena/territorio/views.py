from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #Este es para imprimir pero en el navegador, del paquete django, del módulo http importamos
#El HttpResponseRedirect, me redirige a otra ruta
from .models import Aprendiz, Monitorias, Actividades
from django.urls import reverse

# Ya mostramos vistas en el navegador

def index(request):
    return render(request, 'territorio/index.html')#Así traemos los templates

def listarAprendiz(request):
    q = Aprendiz.objects.all()
    contexto = {'datos': q }#Esta es la variable que se utiliza al final de el render
    return render(request, 'territorio/aprendiz/listar_aprendiz.html', contexto)

def insertarAprendiz(request):
        return render(request, 'territorio/aprendiz/crear_aprendiz.html')

def guardarAprendiz(request):
    try:
        q = Aprendiz(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            cedula = request.POST["cedula"],
            fecha_nacimiento = request.POST["fecha_nacimiento"],
        )
        q.save()
        #return HttpResponse ("Aprendiz agregado correctamente <br/><a href='../aprendiz/'>Lista de aprendices</a>")
        return HttpResponseRedirect(reverse('territorio:aprendiz'))# args() El reverse tiene 2 parámetro, la url de a dónde quiero que vaya y argumentos, si no necesita datos, no es necesario poner los argumentos
    except Exception as e:
        return HttpResponse("Error" + str(e))

def listarMonitorias(request):
    m = Monitorias.objects.all()
    contexto = {'datos': m}
    return render(request, 'territorio/monitorias/listar_monitorias.html', contexto)

def insertarMonitoria(request):
    a = Aprendiz.objects.all()
    contexto = {'aprendiz': a}
    return render(request, 'territorio/monitorias/agregar_monitoria.html', contexto)
    
def guardarMonitoria(request):
    try:
        a = Aprendiz.objects.get(pk = request.POST["aprendiz"])
        q = Monitorias(
            cat = request.POST["cat"],
            aprendiz = a,
            fechaInicio = request.POST["fechaInicio"],
            fechaFinal = request.POST["fechaFinal"],
        )
        q.save()
        return HttpResponseRedirect(reverse('territorio:monitorias'))
    except Exception as e:
        return HttpResponse("Error" + str(e))
    
def listarActividades(request):
    a = Actividades.objects.all()
    contexto = {'datos': a}
    return render(request, 'territorio/actividades/listar_actividades.html', contexto)

def insertarActividad(request):
    m = Monitorias.objects.all()
    contexto = {'monitorias': m}
    return render(request, 'territorio/actividades/agregar_actividad.html', contexto)
    

def guardarActividad(request):
    try:
        m = Monitorias.objects.get(pk = request.POST["monitoria"])
        q = Actividades(
            monitoria = m,
            actividad = request.POST["actividad"],
            observaciones = request.POST["observaciones"],
            fecha = request.POST["fecha"],
        )
        q.save()
        return HttpResponseRedirect(reverse('territorio:actividades'))
    except Exception as e:
        return HttpResponse("Error" + str(e))
    
