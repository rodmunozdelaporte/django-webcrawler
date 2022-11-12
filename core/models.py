from django.db import models



# Create your models here.
class NewsItem(models.Model):
	titulo = models.CharField(max_length=200)
	fuente = models.CharField(max_length=100)
	link = models.URLField(max_length=200)
	fecha_creado = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.link[0:50]
