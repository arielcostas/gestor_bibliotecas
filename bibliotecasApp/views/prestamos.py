from django.shortcuts import render

from bibliotecasApp.models import Prestamo


def lista_prestamos(request):
	prestamos = Prestamo.objects.all()
	return render(request, 'prestamos/index.html', {'prestamos': prestamos})