from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bibliotecasApp.forms.nuevosocioform import NuevoSocioForm
from bibliotecasApp.models import Socio


def nuevo_socio(request):
	if request.method == 'POST':
		form = NuevoSocioForm(request.POST)
		if form.is_valid():
			Socio.objects.create(
				dni=form.cleaned_data['dni'],
				nombre=form.cleaned_data['nombre'],
				apellidos=form.cleaned_data['apellido'],
				email=form.cleaned_data['email'],
				telefono=form.cleaned_data['telefono'],
				domicilio=form.cleaned_data['domicilio'],
				codigo_postal=form.cleaned_data['codigo_postal'],
				ciudad=form.cleaned_data['ciudad'],
				provincia=form.cleaned_data['provincia'],
				fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
			).save()

			messages.success(request, 'Socio creado correctamente')
			if form.cleaned_data['crear_otro']:
				return HttpResponseRedirect('socios/new')
			else:
				return HttpResponseRedirect('/')
	else:
		form = NuevoSocioForm()
	return render(request, 'socios/new.html', {'form': form})

def perfil_socio(request, dni: str):
	socio = Socio.objects.get(dni=dni)
	return render(request, 'socios/dni.html', {'socio': socio})