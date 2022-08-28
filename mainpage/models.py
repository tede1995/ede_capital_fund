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

class Reports(models.Model):
	title = models.CharField(max_length=255)
	summary = models.TextField()
	download_link = models.URLField(max_length=1000, default='', blank=True)
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_on']
		verbose_name_plural = "Reports"

	def __str__(self):
		return self.title
