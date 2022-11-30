from django.urls import path

from bibliotecasApp import views

urlpatterns = [
	path('', views.busqueda, name='index'),

	path('socios/new', views.nuevo_socio, name='socios_new'),
	path('socios/<str:dni>', views.perfil_socio, name='socios_perfil'),

	path('libros/new', views.nuevo_libro, name='libros_new'),

	path('prestamos', views.lista_prestamos, name='prestamo_index'),
]
