from django import forms
from .models import Hotel, PrecioPorTipo, Habitacion, TemporadaAlta,Descuento,PaqueteTuristico

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class PrecioPorTipoForm(forms.ModelForm):
    class Meta:
        model = PrecioPorTipo
        fields = '__all__'
        
class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'

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

   