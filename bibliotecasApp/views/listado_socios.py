from django.shortcuts import render

from bibliotecasApp.models import Socio


def listado_socios(request):
	socios = Socio.objects.all()
	return render(request, 'socios/index.html', {'socios': socios})
