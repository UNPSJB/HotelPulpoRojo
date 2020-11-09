from django import forms
from .models import Persona, Encargado, Pais, Provincia,Localidad,TipoHabitacion,Rol,Cliente,Vendedor
from django.contrib.auth.models import User

#Formularios de personas
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteForm(PersonaForm):
    class Meta:
        model = Persona
        exclude = [
            'usuario'
        ]

class EncargadoForm(PersonaForm):
    class Meta:
        model = Persona
        exclude = [
            'usuario'
        ]
       
class VendedorForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'tipo_documento',
            'documento',

        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'tipo_documento': 'Tipo de Documento',
            'documento': 'Número de Documento',
            'usuario': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirme la contraseña'
        }
            
class CrearVendedorForm(VendedorForm):
    usuario = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        # localidad = LocalidadForm(self.cleaned_data).save(commit=commit)
        persona = super().save(commit=commit)
        return persona.hacer_vendedor(self.cleaned_data["usuario"], self.cleaned_data["email"], self.cleaned_data["password1"])

    def clean_usuario(self):
        usuario = self.cleaned_data["usuario"]
        if len(usuario)<6:
            raise forms.ValidationError("La longitud mínima para un usuario es de 6 caracteres")
        if " " in usuario:
            raise forms.ValidationError("No seas animal, no pongas espacios")
        if User.objects.filter(username=usuario).exists():
            raise forms.ValidationError("El usuario ya existe")
        return usuario
    
    def clean(self):
        data = super().clean()
        if data["password1"]!=data["password2"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return data

class EditarVendedorForm(VendedorForm):
    pass

#Formularios de zona
class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

#Cosa rara: CrearVendedorForm.base_fields.update(LocalidadForm.base_fields)  Implicaría sobrecargar el save()

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

# class TipoHabitacionForm(forms.ModelForm):
#     class Meta:
#         model = TipoHabitacion
#         fields = [
#             'nombre',
#             'descripcion',
#             'pasajeros',
#             'cuartos',
#         ]
#         labels = {
#             'nombre': 'Nombre',
#             'descripcion': 'Descripcion',
#             'pasajeros': 'Pasajeros',
#             'cuartos': 'Cuartos',
#         }    

# class CrearTipoHabitacionForm(TipoHabitacionForm):
#     nombre = forms.CharField(widget=forms.TextInput)
#     descripcion = forms.CharField(widget=forms.TextInput)
#     pasajeros = forms.IntegerField(widget=forms.NumberInput)

#     def clean_tipoHabitacion(self):
#         tipoHabitacion = self.cleaned_data["nombre"]
#         if len(tipoHabitacion)<6:
#             raise forms.ValidationError("La longitud mínima para un tipo de habitacion es de 6 caracteres")
#         if " " in tipoHabitacion:
#             raise forms.ValidationError("nombre invalido")
#         return tipoHabitacion

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'