from django.contrib import admin
from django.urls import path, include

from bibliotecasApp import views

urlpatterns = [
	path('', views.busqueda, name='index'),
	path('socios', views.busqueda, name='socios/index'),
	path('prestamos', views.busqueda, name='prestamos/index'),
]
