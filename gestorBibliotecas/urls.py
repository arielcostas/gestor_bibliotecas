from django.urls import path

from bibliotecasApp import views

urlpatterns = [
	path('', views.busqueda, name='index'),
	path('prestamos', views.busqueda, name='prestamo_index'),
	path('socios/new', views.nuevo_socio, name='socios_new'),
	path('libros/new', views.nuevo_libro, name='libros_new'),
]
