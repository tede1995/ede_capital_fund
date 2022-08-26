from django.shortcuts import render
from .forms import ContactForm
import logging

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

	form = ContactForm()
	context = {'form': form}

	return render(request, 'mainpage/index.html', context)