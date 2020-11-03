from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .QuadTree import *
from mysite.settings import BASE_DIR
import os

# Create your views here.

def index(request):
	template = loader.get_template('moda/index2.html')
	return HttpResponse(template.render(None, request))

def initgallery(request):
	qt = QuadTree()
	dfQuadtree = pd.read_csv(os.path.join(BASE_DIR, 'moda/static/anno/points.txt'))

	listImgIni = qt.selectImgQuadTree(dfQuadtree, 18)
	context = {'img_list': listImgIni}

	template = loader.get_template('moda/initgallery.html')
	return HttpResponse(template.render(context, request))


def smartgallery(request):
	template = loader.get_template('moda/smartGallery.html')
	return HttpResponse(template.render(None, request))

