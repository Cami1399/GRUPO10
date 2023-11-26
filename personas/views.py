from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from personas.forms import LibroForm
from personas.models import Libro
# Create your views here.

def agregar_libro(request):
    pagina = loader.get_template('agregar_libro.html')
    if request.method == 'GET':
        form = LibroForm
    elif request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libreria')
    datos = {'form':form}
    return HttpResponse(pagina.render(datos,request))

def modificar_libro(request, id):
    pagina = loader.get_template('modificar_libro.html')
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    elif request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libreria')
    datos = {'form': form}
    return HttpResponse(pagina.render(datos, request))

def ver_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    datos = {'libro':libro}
    pagina = loader.get_template('ver_libro.html')
    return HttpResponse(pagina.render(datos, request))

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if libro:
        libro.delete()
        return redirect('libreria')