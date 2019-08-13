from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Hotdog(models.Model):
	title = models.CharField(max_length=500,db_index=True)
	description = models.TextField()
	image = models.ImageField(upload_to='images/',blank=True,null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('hot_dogs_list')