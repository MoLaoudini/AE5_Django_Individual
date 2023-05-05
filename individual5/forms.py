from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor

class FormularioRegistroUsuario(UserCreationForm):

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Correo Electrónico'}))
    first_name = forms.CharField(label="",max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellido'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. Solo puedes usar letras, números y los símbolos @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repetir contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Para verificar, introduzca la misma contraseña anterior.</small></span>'

class FormularioRegistroProveedor(forms.ModelForm):
    nombre = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
    actividad = forms.CharField(label="", max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Actividad'}))
    email = forms.EmailField(label="", max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    telefono = forms.CharField(label="", max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Teléfono'}))

    class Meta:
        model = Proveedor
        fields = ['nombre', 'actividad', 'email', 'telefono']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['email'].help_text = '<span class="form-text text-muted"><small>El email no debe estar registrado anteriormente</small></span>'
        self.fields['telefono'].help_text = '<span class="form-text text-muted"><small>Ingrese teléfono con el siguiente formato: +56 9 12345678</small></span>'

