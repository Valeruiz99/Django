"""sena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Estrategia para separar las urls de las aplicaciones 
#El include quiere decir que todas las vistas de la aplicación territorio, se van a reflejar allí

urlpatterns = [
    path('admin/', admin.site.urls),#Django ya trae una aplicación creada y es admin
    path('territorio/', include('territorio.urls')),
]
#Para agregar rutas se usa la función path, tiene 3 parámetros, 
# 1-Como quiero que el usuario ponga en la barra de direcciones
# 2-Cuál vista quiero abrir.
# 3- un alias de la vista


