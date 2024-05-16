from django.db import models

class Lapicero(models.Model):
	marca 				= models.TextField()
	color 				= models.TextField()
	tipo 		        = models.TextField()
	material 		    = models.TextField()
	def __str__(self):
		return self.marca 