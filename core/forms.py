from django import forms
from .models import Persona, Encargado, Pais, Provincia,Localidad,TipoHabitacion,Rol,Cliente,Vendedor

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class EncargadoForm(forms.ModelForm):
    class Meta:
        model = Encargado
        fields = '__all__'
        
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'    