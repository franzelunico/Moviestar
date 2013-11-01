from principal.models import Formato, Pelicula, Genero, Copia_Formato
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def inicio(require):
	generos = Genero.objects.all()
	peliculas = Pelicula.objects.all()
	t = {'generos': generos, 'peliculas': peliculas}
	return render_to_response('index.html',t)