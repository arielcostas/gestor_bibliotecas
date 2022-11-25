from django.urls import path

from bibliotecasApp import views

urlpatterns = [
	path('', views.busqueda, name='index'),
	path('prestamos', views.busqueda, name='prestamos/index'),
]
