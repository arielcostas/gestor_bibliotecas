from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bibliotecasApp.forms import NuevoLibroForm
from bibliotecasApp.models import Libro


def nuevo_libro(request):
	if request.method == 'POST':
		form = NuevoLibroForm(request.POST)
		if form.is_valid():
			l = Libro.objects.create(
				isbn=form.cleaned_data['isbn'],
				titulo=form.cleaned_data['titulo'],
				autor=form.cleaned_data['autor'],
				editorial=form.cleaned_data['editorial']
			)
			l.save()

			messages.success(request, 'Libro creado correctamente')
			if form.cleaned_data['crear_otro']:
				return HttpResponseRedirect(request.path)
			else:
				return HttpResponseRedirect('/')
	else:
		form = NuevoLibroForm()
	return render(request, 'libros/new.html', {'form': form})
