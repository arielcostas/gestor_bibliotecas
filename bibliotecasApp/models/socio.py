from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Socio(models.Model):
	dni = models.CharField(max_length=9, primary_key=True)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()

	domicilio = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=5)
	ciudad = models.CharField(max_length=50)
	provincia = models.CharField(max_length=50)

	telefono = models.CharField(max_length=9, unique=True, null=True, blank=True)
	email = models.CharField(max_length=200, unique=True)

	fecha_alta = models.DateField(auto_now=True)
	avisos_penalizacion = models.IntegerField(default=0, validators=[MinValueValidator(0),
																	 MaxValueValidator(3)])
	bloqueado_hasta = models.DateField(default=None, null=True, blank=True)

	class Meta:
		verbose_name = 'Socio'
		verbose_name_plural = 'Socios'

	def prestamos_activos(self):
		return self.prestamo_set.filter(fecha_devolucion_real=None).count()

	def prestamos_socio(self):
		return self.prestamo_set.all().order_by("-fecha_prestamo")