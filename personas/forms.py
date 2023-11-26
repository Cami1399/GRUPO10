
from django.forms import ModelForm
from django import forms
from personas.models import Libro, Presentacion, Categoria

# creating a form

class LibroForm(forms.ModelForm):


    class Meta:
        model = Libro
        fields =  [ 'titulo', 'autor', 'Presentacion','Categoria', 'fecha_publicacion', 'sinopsis', 'disponibilidad']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'Presentacion': forms.RadioSelect(attrs={'class': 'radio-button-highlight'}),


        }