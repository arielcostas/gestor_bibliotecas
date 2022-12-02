from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bibliotecasApp.forms import GestionBloqueoForm, NuevoSocioForm
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
				return HttpResponseRedirect(request.path)
			else:
				return HttpResponseRedirect('/')
	else:
		form = NuevoSocioForm()
	return render(request, 'socios/new.html', {'form': form})


def perfil_socio(request, dni: str):
	socio = Socio.objects.get(dni=dni)
	return render(request, 'socios/dni.html', {'socio': socio})


def editar_socio(request, dni: str):
	socio = Socio.objects.get(dni=dni)
	if request.method == 'POST':
		form = NuevoSocioForm(request.POST)
		if form.is_valid():
			socio.dni = form.cleaned_data['dni']
			socio.nombre = form.cleaned_data['nombre']
			socio.apellidos = form.cleaned_data['apellido']
			socio.email = form.cleaned_data['email']
			socio.telefono = form.cleaned_data['telefono']
			socio.domicilio = form.cleaned_data['domicilio']
			socio.codigo_postal = form.cleaned_data['codigo_postal']
			socio.ciudad = form.cleaned_data['ciudad']
			socio.provincia = form.cleaned_data['provincia']
			socio.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
			socio.save()

			messages.success(request, 'Socio editado correctamente')
			return HttpResponseRedirect('/socios/' + dni)
	else:
		form = NuevoSocioForm(initial={
			'dni': socio.dni,
			'nombre': socio.nombre,
			'apellido': socio.apellidos,
			'email': socio.email,
			'telefono': socio.telefono,
			'domicilio': socio.domicilio,
			'codigo_postal': socio.codigo_postal,
			'ciudad': socio.ciudad,
			'provincia': socio.provincia,
			'fecha_nacimiento': socio.fecha_nacimiento,
		})
	return render(request, 'socios/edit.html', {'form': form, 'socio': socio})


def bloquear_socio(request, dni: str):
	socio = Socio.objects.get(dni=dni)
	if request.method == 'POST':
		form = GestionBloqueoForm(request.POST)
		if form.is_valid():
			socio.avisos_penalizacion = form.cleaned_data['cantidad_avisos']
			if form.cleaned_data['activar_bloqueo']:
				socio.bloqueado_hasta = form.cleaned_data['fecha_bloqueo']
			else:
				socio.bloqueado_hasta = None
			socio.save()

			messages.success(request, 'Socio bloqueado correctamente')
			return HttpResponseRedirect('/socios/' + dni)
		else:
			messages.error(request, 'Error al bloquear el socio')
			return HttpResponseRedirect('/socios/' + dni)
	return HttpResponseRedirect('/socios/' + dni)
