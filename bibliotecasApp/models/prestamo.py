from datetime import date

from django.db import models

from bibliotecasApp.models import Socio, Libro


class Prestamo(models.Model):
	id = models.AutoField(primary_key=True)
	fecha_prestamo = models.DateField()
	fecha_devolucion = models.DateField()
	fecha_devolucion_real = models.DateField(blank=True, null=True)
	socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
	libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Prestamo'
		verbose_name_plural = 'Prestamos'

	def pendiente_tarde(self):
		if self.fecha_devolucion_real is None and self.fecha_devolucion <= date.today():
			return True
		return False

	def get_libro(self) -> Libro:
		return self.libro

	def get_socio(self) -> Socio:
		return self.socio
