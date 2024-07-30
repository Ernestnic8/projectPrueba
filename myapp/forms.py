from django import forms
from .models import Empleados,Libro, Clientes

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model= Empleados
        fields = ('__all__')

class LibroForm(forms.ModelForm):
    class Meta:
        model= Libro
        fields=('__all__')
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'required': False}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Clientes
        fields = ('__all__')