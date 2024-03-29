from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import ContactForm
from .models import Reports, Team, Content, ChartData
import logging

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			email_subject = f'New contact : {form.cleaned_data["name"]} - {form.cleaned_data["email"]} - {form.cleaned_data["phonenumber"]} - {form.cleaned_data["subject"]}'
			email_message = form.cleaned_data['message']
			send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
			return render(request, 'mainpage/success.html')

	form = ContactForm()

	report = Reports.objects.all()

	team = Team.objects.all()

	content = Content.objects.all()

	# Handle Chart Date

	labels = []
	data = []
	data_2 = []

	queryset = ChartData.objects.all()[:12]
	for chart in queryset:
		labels.append(chart.month)
		data.append(chart.fund_performance)
		data_2.append(chart.market_performance)

	# Handle Chart Date

	context = {'form': form, 'reports': report, 'team': team, 'content': content, 'labels': labels, 'data': data, 'data_2': data_2,}

	return render(request, 'mainpage/index.html', context)

def success_view(request):

	return render(request, 'mainpage/success.html')

def handler404(request, exception):
    return render(request, 'mainpage/404.html', status=404)

def handler500(request):
    return render(request, 'mainpage/404.html', status=500)