from django import forms
from .models import Categoria

class categoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = ['nombre', 'imagen']

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre de la categoría'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'URL de la imagen de la categoría'
                }
            )
        }

        labels = {
            'nombre': 'Nombre de la categoría',
            'imagen': 'URL de la imagen de la categoría'
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre de la categoría es obligatorio',
            },
            'imagen': {
                'required': 'La URL de la imagen de la categoría es obligatoria',
            }
        }