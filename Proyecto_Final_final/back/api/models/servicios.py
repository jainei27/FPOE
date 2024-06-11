from django.db import models

class Servicios(models.Model):
	nombre		= models.CharField(max_length=50)
	cedula      = models.TextField()
	descripcion = models.TextField()
	valor	    = models.TextField()
	

	def __str__(self):
		return self.nombre