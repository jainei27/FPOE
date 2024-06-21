from django.db import models

class Cliente(models.Model):
	nombre		= models.CharField(max_length=50)
	apellido    = models.TextField()
	cedula 		= models.IntegerField()
	telefono	= models.IntegerField()
	correo      = models.TextField()

	def __str__(self):
		return self.nombre