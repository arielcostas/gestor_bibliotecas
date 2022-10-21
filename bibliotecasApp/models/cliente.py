from django.db import models


class Cliente(models.Model):
	dni = models.CharField(max_length=9, unique=True, primary_key=True)
	nombre = models.CharField(max_length=50)
	fechaAlta = models.DateField(auto_now_add=True)
	telefono = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
