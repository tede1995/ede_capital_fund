from django.shortcuts import render
from .forms import ContactForm
from .models import Reports, Team, Content
import logging

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

			# Insert code to send email to admin containing form details. 
			# Q: Purpose for email marketing? If so attach a SendGrid API.

	form = ContactForm()

	report = Reports.objects.all()

	team = Team.objects.all()

	content = Content.objects.all()

	context = {'form': form, 'reports': report, 'team': team, 'content': content}

	return render(request, 'mainpage/index.html', context)