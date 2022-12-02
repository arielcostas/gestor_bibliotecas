from django.shortcuts import render

from bibliotecasApp.models import Prestamo


def lista_prestamos(request):
	prestamos = Prestamo.objects.filter(fecha_devolucion_real__isnull=True)
	return render(request, 'prestamos/index.html', {'prestamos': prestamos})