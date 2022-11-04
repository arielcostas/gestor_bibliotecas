from django.db import models


class Libro(models.Model):
	isbn = models.CharField(max_length=13, primary_key=True)
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=50)
	editorial = models.CharField(max_length=50)
	fecha_publicacion = models.DateField()
	genero = models.CharField(max_length=50)
	idioma = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)

	class Meta:
		verbose_name = 'Libro'
		verbose_name_plural = 'Libros'