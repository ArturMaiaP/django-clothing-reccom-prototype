from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
	template = loader.get_template('moda/index.html')
	return HttpResponse(template.render(None, request))

def initgallery(request):
	template = loader.get_template('moda/initgallery.html')
	return HttpResponse(template.render(None, request))

def smartgallery(request):
	template = loader.get_template('moda/smartGallery.html')
	return HttpResponse(template.render(None, request))