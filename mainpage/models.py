from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	phonenumber = models.CharField(max_length=14)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.email