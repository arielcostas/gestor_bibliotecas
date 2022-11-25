from enum import Enum

from django.shortcuts import render

from bibliotecasApp.models import Libro, Socio


def busqueda(request):
	"""Listado de resultados"""
	query = request.GET.get("query")

	# Busca los resultados que contengan la cadena query en el título o en el autor
	libros: list[Libro] = None
	socios: list[Socio] = None
	if query and len(query) > 0:
		libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(
			autor__icontains=query) | Libro.objects.filter(
			editorial__icontains=query)
		socios = Socio.objects.filter(nombre__icontains=query) | Socio.objects.filter(
			apellidos__icontains=query) | Socio.objects.filter(
			dni__icontains=query) | Socio.objects.filter(
			email__icontains=query) | Socio.objects.filter(telefono__icontains=query)
	else:
		libros = Libro.objects.all()
		socios = Socio.objects.all()

	return render(request, 'index.html', {'libros': libros, 'socios': socios, 'query': query if query else ''})
