from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django_ajax.decorators import ajax
from django.views.decorators.csrf import csrf_exempt

from .QuadTree import *
from mysite.settings import BASE_DIR
import os

# Create your views here.

def index(request):
	template = loader.get_template('moda/index.html')
	return HttpResponse(template.render(None, request))

def initgallery(request):
	qt = QuadTree()
	dfQuadtree = pd.read_csv(os.path.join(BASE_DIR, 'moda/static/anno/points.txt'))

	listImgIni = qt.selectImgQuadTree(dfQuadtree, 12)
	context = {'img_list': listImgIni}

	template = loader.get_template('moda/infiniteGallery.html')
	return HttpResponse(template.render(context, request))

@csrf_exempt
def moreImages(request):
    listRel = request.POST.getlist("listRel[]")
    listIrrel = request.POST.getlist("listIrrel[]")
    print("####### IMAGENS ESCOLHIDAS #######")
    print(listRel)
    print(listIrrel)
    print("########## ############ #########")

    qt = QuadTree()
    dfQuadtree = pd.read_csv(os.path.join(BASE_DIR, 'moda/static/anno/points.txt'))
    listImgIni = qt.selectImgQuadTree(dfQuadtree, 12)

    context = {'img_list': listImgIni}
    template = loader.get_template('moda/moreImages.html')
    return HttpResponse(template.render(context, request))
