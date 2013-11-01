#encoding:utf-8
from django.db import models

#Poner 3d y 2d como campo de seleccion (como sexo) para hacer mas eficiente la busqueda en la BD
class Formato(models.Model):
	nombre_formato		= models.CharField(max_length=50)
	def __unicode__(self):
		return self.nombre_formato

class Genero(models.Model):
	nombre_genero		= models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre_genero

class Pelicula(models.Model):
	titulo_pelicula		= models.CharField(max_length=100)
	descripcion_pelicula	= models.TextField(max_length=500, help_text='Redacta la sinopsis de la pelicula')
#	imagen_pel		= models.ImageField(upload_to='peliculas', verbose_name='imagen_pel')
	genero_pelicula		= models.ForeignKey('Genero')

	def __unicode__(self):
		return self.titulo_pelicula

class Copia_Formato(models.Model):
	cantidad_copia		= models.IntegerField()
	precio_copia		= models.FloatField()
	pelicula_copia		= models.ForeignKey('Pelicula')
	formato_copia		= models.ForeignKey('Formato')

	def __unicode__(self):
		msg = '"'+ self.pelicula_copia.titulo_pelicula +'"' + ' en formato ' + self.formato_copia.nombre_formato
		return msg
class Director(models.Model):
    nombre_director     = models.CharField(max_length=50)
    def __unicode__(self):
		return self.nombre_director
class Actor(models.Model):
    nombre_actor     =  models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre_actor
class Actua(models.Model):
    pelicula_actua = models.ForeignKey('Pelicula')
    actor_actua    = models.ForeignKey('Actor')

    def __unicode__(self):
        msg = self.actor_actua.nombre_actor +'actua en ' +'"'+ self.pelicula_actua.titulo_pelicula
        return msg

