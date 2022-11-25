from django.http import HttpResponseRedirect
from django.shortcuts import render

from bibliotecasApp.forms import NuevoLibroForm
from bibliotecasApp.models import Libro


def nuevo_libro(request):
	if request.method == 'POST':
		form = NuevoLibroForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			l = Libro.objects.create(
				isbn=form.cleaned_data['isbn'],
				titulo=form.cleaned_data['titulo'],
				autor=form.cleaned_data['autor'],
				editorial=form.cleaned_data['editorial']
			)
			l.save()

			if form.cleaned_data['crear_otro']:
				return HttpResponseRedirect('socios/new')
			else:
				return HttpResponseRedirect('/')
	else:
		form = NuevoLibroForm()
	return render(request, 'libros/new.html', {'form': form})