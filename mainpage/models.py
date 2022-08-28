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

class Team(models.Model):
	fullname = models.CharField(max_length=255)
	position = models.CharField(max_length=500)
	profile_image_url = models.URLField(max_length=1000, default='', blank=True)
	linkedin_url = models.URLField(max_length=1000, default='', blank=True)
	hierarchy = models.IntegerField()
	position_adjustment = models.TextField(max_length=800, blank=True)

	class Meta:
		ordering = ['hierarchy']
		verbose_name_plural = "Team"

	def __str__(self):
		return self.fullname

class Content(models.Model):
	website_title = models.CharField(max_length=600)
	homepage_title = models.CharField(max_length=1000)
	homepage_subtitle = models.TextField()
	performance_title = models.CharField(max_length=1000)
	performance_subtitle = models.TextField()
	strategy_title = models.CharField(max_length=1000)
	strategy_subtitle = models.TextField()
	strategy_card_title_1 = models.CharField(max_length=1000)
	strategy_card_title_2 = models.CharField(max_length=1000)
	strategy_card_title_3 = models.CharField(max_length=1000)
	strategy_card_content_1 = models.TextField()
	strategy_card_content_2 = models.TextField()
	strategy_card_content_3 = models.TextField()
	team_title = models.CharField(max_length=1000)
	team_subtitle = models.TextField()
	contact_title = models.CharField(max_length=1000)
	contact_subtitle = models.TextField()
	disclaimer = models.TextField()

	class Meta:
		verbose_name_plural = "Content"

	def __str__(self):
		return self.website_title
