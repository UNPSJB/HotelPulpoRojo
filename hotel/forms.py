from django import forms
from core.models import Persona, Encargado, Vendedor
from .models import Hotel, PrecioPorTipo, Habitacion, TemporadaAlta,Descuento,PaqueteTuristico
from django.http import request
from datetime import date, datetime

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
    
class AsignarForm(forms.Form): 
    vendedores = forms.ModelChoiceField(
            queryset= Vendedor.objects.all(),
            label="Vendedores",
            widget= forms.Select(attrs={
                'placeholder':'Seleccione un vendedor'
            })
        )
    
    def save(self, hotel):    
        vendedor = self.data.get('vendedores')     
        hotel.vendedores.add(vendedor)
        return hotel
        


class PrecioPorTipoForm(forms.ModelForm):
    class Meta:
        model = PrecioPorTipo
        fields = '__all__'
        
class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'
        widgets = {'hotel':forms.HiddenInput}

class DateInput(forms.DateInput):
    input_type = 'date'

class TemporadaAltaForm(forms.ModelForm):
    class Meta:
        model = TemporadaAlta
        fields = '__all__'
        widgets = {'hotel':forms.HiddenInput}
    
    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('inicio')
        fin = cleaned_data.get('fin')
        
        # Validacion de fechas ingresadas
        if inicio.year == fin.year:
            if inicio.month == fin.month:
                # validar que el dia de inicio no sea mayor al de fin
                if inicio.day > fin.day:
                    raise forms.ValidationError("La fecha ingresada en fin es inferior a la de inicio")
                # validar que el dia de inicio y fin no sean iguales
                if inicio.day == fin.day:
                    raise forms.ValidationError("El dia de inicio y fin no pueden ser iguales")
            # validar que el mes de inicio no sea mayor al de fin en el mismo año    
            if inicio.month > fin.month:
                raise forms.ValidationError("La fecha ingresada en fin es inferior a la de inicio")
            # validar que el mes de inicio no sea menor al del mes actual
            if inicio.month < datetime.now().month:
                raise forms.ValidationError("La fecha de inicio es inferior a la actual")
            # validar que el mes de fin no sea mayor al del mes actual
            if fin.month < datetime.now().month:
                raise forms.ValidationError("La fecha de fin es inferior a la actual")
        # validar que el año de inicio no sea menor que el del año actual
        if inicio.year < datetime.now().year:
            raise forms.ValidationError("La fecha de inicio es inferior a la actual")
        # validar que el año de fin no sea menor que el actual
        if fin.year < datetime.now().year:
            raise forms.ValidationError("La fecha de fin es inferior a la actual")
        
        

class DescuentoForm(forms.ModelForm):
    class Meta:
        model = Descuento
        fields = '__all__'

class PaqueteTuristicoForm(forms.ModelForm):
    class Meta:
        model = PaqueteTuristico
        exclude = ['hotel']

    