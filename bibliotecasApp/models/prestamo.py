from django.db import models


class Prestamo(models.Model):
	id = models.AutoField(primary_key=True)
	fecha_prestamo = models.DateField()
	fecha_devolucion = models.DateField()
	fecha_devolucion_real = models.DateField()
	socio = models.ForeignKey('Socio', on_delete=models.CASCADE)
	libro = models.ForeignKey('Libro', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Prestamo'
		verbose_name_plural = 'Prestamos'
