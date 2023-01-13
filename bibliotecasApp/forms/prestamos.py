from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import forms, CharField, DateField


class NuevoPrestamoForm(forms.Form):
	socio = CharField(
		label='Socio',
		validators=[
			MinLengthValidator(9),
			MaxLengthValidator(9),
		],
	)
	libro = CharField(
		label='Libro',
	)
	fecha_devolucion = DateField(
		label='Fecha de devolución',
	)
