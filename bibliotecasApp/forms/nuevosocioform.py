from django.core.validators import *
from django.forms import forms, BooleanField


class NuevoSocioForm(forms.Form):
	dni = forms.Field(label='DNI', validators=[MinLengthValidator(9), MaxLengthValidator(9)])
	nombre = forms.Field(label='Nombre', validators=[MinLengthValidator(3), MaxLengthValidator(50)])
	apellido = forms.Field(label='Apellido', validators=[MinLengthValidator(3), MaxLengthValidator(50)])
	fecha_nacimiento = forms.Field(label='Fecha de nacimiento', validators=[])
	email = forms.Field(label='Email', validators=[EmailValidator()])
	telefono = forms.Field(label='Telefono', validators=[MinLengthValidator(9), MaxLengthValidator(9)])
	domicilio = forms.Field(label='Direccion', validators=[MinLengthValidator(3), MaxLengthValidator(100)])
	codigo_postal = forms.Field(label='Codigo Postal', validators=[MinLengthValidator(5), MaxLengthValidator(5)])
	ciudad = forms.Field(label='Ciudad', validators=[MinLengthValidator(3), MaxLengthValidator(50)])
	provincia = forms.Field(label='Provincia', validators=[MinLengthValidator(3), MaxLengthValidator(50)])

	crear_otro = BooleanField(label='Crear otro socio', required=False)
