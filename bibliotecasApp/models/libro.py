from django.db import models


class Libro(models.Model):
	codigo = models.AutoField(primary_key=True)
	isbn = models.CharField(max_length=13)
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	editorial = models.CharField(max_length=50)
	fecha_adquisicion = models.DateField(auto_now=True)

	class Meta:
		verbose_name = 'Libro'
		verbose_name_plural = 'Libros'