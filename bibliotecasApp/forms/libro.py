from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import forms, BooleanField


class NuevoLibroForm(forms.Form):
	isbn = forms.Field(label='ISBN', validators=[MinLengthValidator(13), MaxLengthValidator(13)])
	titulo = forms.Field(label='Titulo', validators=[MinLengthValidator(3), MaxLengthValidator(100)])
	autor = forms.Field(label='Autor', validators=[MinLengthValidator(3), MaxLengthValidator(50)])
	editorial = forms.Field(label='Editorial', validators=[MinLengthValidator(3), MaxLengthValidator(50)])

	crear_otro = BooleanField(label='Crear otro socio', required=False)
