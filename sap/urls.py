"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from webapp.views import libreria
from personas.views import agregar_libro, ver_libro, eliminar_libro, modificar_libro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', libreria, name='libreria'),
    path('agregar_libro/',agregar_libro, name='agregar_libro'),
    path('eliminar_libro/<int:id>/', eliminar_libro, name='eliminar_libro'),
    path('modificar_libro/<int:id>/', modificar_libro, name='modificar_libro'),
    path('ver_libro/<int:id>/', ver_libro, name='ver_libro'),
]

