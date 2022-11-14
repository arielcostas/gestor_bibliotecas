from django.db import models


class Libro(models.Model):
	codigo = models.IntegerField(primary_key=True, auto_created=True)
	isbn = models.CharField(max_length=13)
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	editorial = models.CharField(max_length=50)
	fecha_adquisicion = models.DateField()

	class Meta:
		verbose_name = 'Libro'
		verbose_name_plural = 'Libros'