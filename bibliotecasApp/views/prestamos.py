from datetime import datetime, timedelta

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from bibliotecasApp.forms.prestamos import NuevoPrestamoForm
from bibliotecasApp.models import Prestamo, Socio, Libro


def lista_prestamos(request):
	prestamos = Prestamo.objects.filter(fecha_devolucion_real__isnull=True)
	return render(request, 'prestamos/index.html', {'prestamos': prestamos})


def nuevo_prestamo(request):
	if request.method == 'POST':
		form = NuevoPrestamoForm(request.POST)
		if form.is_valid():
			l = Libro.objects.get(codigo=form.cleaned_data['libro'])
			s = Socio.objects.get(dni=form.cleaned_data['socio'])

			if l.is_prestado():
				messages.error(request, 'El libro ya está prestado')
			elif s.bloqueado_hasta is not None:
				if s.bloqueado_hasta > datetime.now().date():
					messages.error(request, 'El socio está bloqueado')
				else:
					s.bloqueado_hasta = None
					s.save()
			else:
				Prestamo.objects.create(
					libro=l,
					socio=s,
					fecha_prestamo=datetime.now(),
					fecha_devolucion=form.cleaned_data['fecha_devolucion'],
				).save()

				messages.success(request, 'Préstamo realizado correctamente.')
				return HttpResponseRedirect('/')
	else:
		form = NuevoPrestamoForm()

	form.fields['fecha_devolucion'].initial = datetime.now().date().replace(month=datetime.now().date().month + 1)
	socios = Socio.objects.all().filter(bloqueado_hasta=None)
	libros = Libro.objects.all()
	libros = [l for l in libros if not l.is_prestado()]
	return render(request, 'prestamos/new.html', {'form': form, 'libros': libros, 'socios': socios})
