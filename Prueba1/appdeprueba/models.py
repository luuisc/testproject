from django.db import models

# Create your models here.
class Alumno(models.Model):
	name = models.CharField()

class Maestro(models.Model):
	name = models.CharField()

class Puta(models.Model)
	apellido = models.CharField()