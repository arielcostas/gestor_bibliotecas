from django.shortcuts import render

from bibliotecasApp.models import Libro


def libros_index(request):
	libros = Libro.objects.all()
	return render(request, 'libros/index.html', {'libros':libros})
