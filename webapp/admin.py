
from django.contrib import admin

# Register your models here.

from personas.models import Libro,Presentacion, Categoria

# Register your models here.
admin.site.register(Libro)
admin.site.register(Presentacion)
admin.site.register(Categoria)