from django.shortcuts import render

# Create your views here.
def lista_clientes(request):
	return render(request, 'clientes.html')