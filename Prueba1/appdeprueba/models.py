from django.db import models

# Create your models here.
class Alumno(models.Model):
	name = models.CharField()
	
class Maestro(models.Model):
	name = models.CharField()

class Clase(models.Model):
	classroom = models.IntegerField()