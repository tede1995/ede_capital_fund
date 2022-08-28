from django.shortcuts import render
from .forms import ContactForm
from .models import Reports, Team
import logging

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

	form = ContactForm()

	report = Reports.objects.all()

	team = Team.objects.all()

	context = {'form': form, 'reports': report, 'team': team}

	return render(request, 'mainpage/index.html', context)