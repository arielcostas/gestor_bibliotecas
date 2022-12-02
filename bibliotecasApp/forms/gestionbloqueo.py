from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class GestionBloqueoForm(forms.Form):
	cantidad_avisos = forms.IntegerField(label='Cantidad de avisos', validators=[MinValueValidator(0), MaxValueValidator(5)])
	activar_bloqueo = forms.BooleanField(label='Activar bloqueo', required=False)
	fecha_bloqueo = forms.DateField(label='Fecha de bloqueo', required=False)