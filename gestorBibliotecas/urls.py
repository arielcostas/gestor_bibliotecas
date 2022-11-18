from django.contrib import admin
from django.urls import path, include

from bibliotecasApp import views

urlpatterns = [
	path('', views.busqueda, name='index'),
	path('libros', views.libros_index, name='libros/index'),
	path('socios', views.socios_index, name='socios/index'),
	path('prestamos', views.busqueda, name='prestamos/index'),
]
