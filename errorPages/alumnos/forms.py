from django import forms
from .models import Alumno

class alumnoForm(forms.ModelForm):
    #Meta es la clase que define la meta-información del formulario
    class Meta:
        #Campo del que se basa el formulario
        model = Alumno

        #Que campos se van a ver en el formulario
        fields = ['nombre','apellido','edad','matricula','correo']

        #Personalizar la apariencia del formulario (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre(s)'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Apelldo(s)'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Edad'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Matricula'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Correo electrónico'
                }
            )
        }

        labels = {
            'nombre': 'Nombre(s)',
            'apellido': 'Apellido(s)',
            'edad': 'Edad',
            'matricula': 'Matricula',
            'correo': 'Correo electrónico'
        }

