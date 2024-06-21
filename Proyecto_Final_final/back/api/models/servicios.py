from django.db import models

class Servicios(models.Model):
	nombre		= models.CharField(max_length=50)
	cedula      = models.IntegerField()
	descripcion = models.TextField()
	valor	    = models.IntegerField()
	

	def __str__(self):
		return self.nombre