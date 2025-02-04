from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo institucional',
                    'required': True,
                    'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debe ingresar un correo válido de la UTEZ (@utez.edu.mx)'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': True,
                    'pattern': r'^[a-zA-Z]+(?: [a-zA-Z]+)*$',   
                    'title': 'Solo se permiten letras en el nombre'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'required': True,
                    'pattern': r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+(?: [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+)*$',
                    'title': 'Solo se permiten letras en el apellido'
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula',
                    'required': True,
                    'pattern': r'^[a-zA-Z0-9]{10,11}$',
                    'title': 'Solo se permiten letras y números en la matrícula y entre 10 o 11 caracteres'
                }
            ),
             'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                    'min': 15, 
                    'max': 60,       
                    'title': 'Debe ingresar una edad válida'
                }
            ),
             'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',
                    'required': True,
                    'pattern': r'^\d{10}$',
                    'title': 'Debe ingresar un número de teléfono válido de al menos 10 dígitos'
                }
            ),
             'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                }
            ),
             'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña igual',
                    'required': True,
                }
            ),
        }

class CustomUserLoginForm(AuthenticationForm):
    pass


class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(label="Correo electrónico", max_length=10)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        
        return cleaned_data

        