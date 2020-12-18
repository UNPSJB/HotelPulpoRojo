from django import forms
from .models import Factura, Alquiler, Liquidacion
from core.models import Persona, Cliente, Vendedor
from hotel.models import Habitacion
from django.http import request

class AlquilerForm(forms.ModelForm):
    # habitacion = forms.CharField(label='Habitación:')
    nombreCliente = forms.CharField(label='Nombre del Cliente:')
    apellidoCliente = forms.CharField(label='Apellido del Cliente:')
    tipodocumentoCliente = forms.ChoiceField(label='Tipo de Documento:', choices=Persona.TIPOS_DOCUMENTO)
    documentoCliente = forms.IntegerField( label='Documento:')
    vendedor = forms.CharField(label='Vendedor:', widget=forms.HiddenInput())
    class Meta:
        model = Alquiler
        exclude = [
            # 'habitaciones',
            'factura',
            'paquete'
        ]
    
    def clean(self):
        cleaneddata = super().clean()
        return cleaneddata

    def __init__(self, *args, **kwargs):
        # Primero llamar a super. 
        super().__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields['nombreCliente'].initial = self.instance.cliente.persona.nombre
            self.fields['apellidoCliente'].initial = self.instance.cliente.persona.apellido
            self.fields['tipodocumentoCliente'].initial = self.instance.cliente.persona.tipo_documento
            self.fields['documentoCliente'].initial = self.instance.cliente.persona.documento
    
    def save(self, commit=True):    
        cliente = Persona.objects.create(
            nombre = self.cleaned_data['nombreCliente'],
            apellido = self.cleaned_data['apellidoCliente'],
            tipo_documento = self.cleaned_data['tipodocumentoCliente'],
            documento = self.cleaned_data['documentoCliente'])
        
        seller = Vendedor.objects.get(id=self.cleaned_data['vendedor'])
        factura = Factura.objects.create(
            cliente = cliente.hacer_cliente(),
            vendedor = seller
            
        )
        factura.save()
        
        #INTENTO DE IMPLEMENTACIÓN DEL MÉTODO DEL MODELO.
        #Creamos el diccionario:
        # habitaciones_con_fecha = {
        #     'habitacion': self.cleaned_data['habitaciones'],
        #     'huespedes': self.cleaned_data['cantidad_huespedes'],
        #     'desde': self.cleaned_data['inicio'],
        #     'hasta': self.cleaned_data['fin']}
        # factura.alquilar_habitaciones(habitaciones_con_fecha)

        # Nuestro save:
        alquiler = super().save(commit=False)
        alquiler.factura = factura
        alquiler.save()
        # alquiler.habitaciones=self.cleaned_data['habitaciones']   #Así no se añaden habitaciones
        for habitacion in self.cleaned_data['habitaciones']:
            alquiler.habitaciones.add(habitacion)
        return alquiler
