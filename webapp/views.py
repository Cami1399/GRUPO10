
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from personas.models import Libro

# Create your views here.
def libreria(request):
    cantidad_libros = Libro.objects.count()
    libros = Libro.objects.order_by('titulo', 'autor', 'Categoria')
    dict_datos = {'cantidad_personas':cantidad_libros, 'libros':libros}
    pagina = loader.get_template('libreria.html')
    return HttpResponse(pagina.render(dict_datos, request))