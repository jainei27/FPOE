from django.db import models

class Mascota(models.Model):

	nombre			= models.CharField(max_length=50)
	altura          = models.FloatField()
	edad            = models.IntegerField()
	raza            = models.TextField()
	def __str__(self):
		return self.nombre