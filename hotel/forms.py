from django import forms
from core.models import Persona, Encargado
from .models import Hotel, PrecioPorTipo, Habitacion, TemporadaAlta,Descuento,PaqueteTuristico
from django.http import request

class HotelForm(forms.ModelForm):
    nombreEncargado = forms.CharField(label='Nombre del Encargado:')
    apellidoEncargado = forms.CharField(label='Apellido del Encargado:')
    tipodocumentoEncargado = forms.ChoiceField(label='Tipo de Documento:', choices=Persona.TIPOS_DOCUMENTO)
    documentoEncargado = forms.IntegerField( label='Documento:')
    class Meta:
        model = Hotel
        exclude = [
            'tipos',
            'vendedores',
            'encargado'
        ]
    
    def clean(self):
        cleaneddata = super().clean()
        return cleaneddata

    def __init__(self, *args, **kwargs):
        # Primero llamar a super. 
        super().__init__(*args, **kwargs)
        print(self.instance.pk)
        if self.instance.pk is not None:
            self.fields['nombreEncargado'].initial = self.instance.encargado.persona.nombre
            self.fields['apellidoEncargado'].initial = self.instance.encargado.persona.apellido
            self.fields['tipodocumentoEncargado'].initial = self.instance.encargado.persona.tipo_documento
            self.fields['documentoEncargado'].initial = self.instance.encargado.persona.documento
        

    #Guardamos al hotel usando el método afiliar_hotel para vincular el hotel y el encargado
    def save(self, commit=True):    
        hotel = super().save(commit=False)
        # Crear encargado
        persona = Persona.objects.create(
            nombre = self.cleaned_data['nombreEncargado'],
            apellido = self.cleaned_data['apellidoEncargado'],
            tipo_documento = self.cleaned_data['tipodocumentoEncargado'],
            documento = self.cleaned_data['documentoEncargado'])        
        # Guardar encargado en el hotel
        hotel.encargado = persona.hacer_encargado()
        hotel.save()
        return hotel
    



class PrecioPorTipoForm(forms.ModelForm):
    class Meta:
        model = PrecioPorTipo
        fields = '__all__'
        
class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class TemporadaAltaForm(forms.ModelForm):
    class Meta:
        model = TemporadaAlta
        fields = '__all__'

class DescuentoForm(forms.ModelForm):
    class Meta:
        model = Descuento
        fields = '__all__'

class PaqueteTuristicoForm(forms.ModelForm):
    class Meta:
        model = PaqueteTuristico
        fields = '__all__'

   