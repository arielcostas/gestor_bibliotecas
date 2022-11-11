from django.shortcuts import render

from bibliotecasApp.models import Libro


def listado_libros(request):
	"""Listado de libros"""
	libros = Libro.objects.all()
	print(libros)
	return render(request, 'index.html', {'libros': libros})