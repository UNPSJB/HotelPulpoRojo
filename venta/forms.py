from django import forms
from .models import Factura, Alquiler, Liquidacion
from core.models import Persona, Cliente
from django.http import request

class AlquilerForm(forms.ModelForm):
    nombreCliente = forms.CharField(label='Nombre del Cliente:')
    apellidoCliente = forms.CharField(label='Apellido del Cliente:')
    tipodocumentoCliente = forms.ChoiceField(label='Tipo de Documento:', choices=Persona.TIPOS_DOCUMENTO)
    documentoCliente = forms.IntegerField( label='Documento:')
    class Meta:
        model = Alquiler
        exclude = [
            'factura',
            'paquete',
            'fue_pagado'
        ]
    
    def clean(self):
        cleaneddata = super().clean()
        return cleaneddata

    def __init__(self, *args, **kwargs):
        # Primero llamar a super. 
        super().__init__(*args, **kwargs)
        print(self.instance.pk)
        if self.instance.pk is not None:
            self.fields['nombreCliente'].initial = self.instance.cliente.persona.nombre
            self.fields['apellidoCliente'].initial = self.instance.cliente.persona.apellido
            self.fields['tipodocumentoCliente'].initial = self.instance.cliente.persona.tipo_documento
            self.fields['documentoCliente'].initial = self.instance.cliente.persona.documento
