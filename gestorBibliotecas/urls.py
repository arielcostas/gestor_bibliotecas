from django.contrib import admin
from django.urls import path, include

from bibliotecasApp import views

urlpatterns = [
	path('', views.listado_libros, name='index'),
	path('socios', views.listado_libros, name='socios/index'),
	path('prestamos', views.listado_libros, name='prestamos/index'),
]
