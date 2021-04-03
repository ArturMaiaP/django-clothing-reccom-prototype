from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django_ajax.decorators import ajax
from django.views.decorators.csrf import csrf_exempt

import pandas as pd
import os
from .QuadTree import *
from mysite.settings import BASE_DIR
import os

# Create your views here.


def index(request):
    template = loader.get_template('moda/index.html')
    return HttpResponse(template.render(None, request))


def init_gallery(request):
    qt = QuadTree()
    df_quadtree = pd.read_csv(os.path.join(BASE_DIR, 'moda/static/anno/points.txt'))

    list_img_ini = qt.select_img_quadtree(df_quadtree, 12)
    context = {'img_list': list_img_ini}

    template = loader.get_template('moda/infiniteGallery.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
def more_images(request):
    list_rel = request.POST.getlist("listRel[]")
    list_irrel = request.POST.getlist("listIrrel[]")
    print("####### IMAGENS ESCOLHIDAS #######")
    print(list_rel)
    print(list_irrel)
    print("########## ############ #########")

    qt = QuadTree()
    df_quadtree = pd.read_csv(os.path.join(BASE_DIR, 'moda/static/anno/points.txt'))
    list_img_ini = qt.select_img_quadtree(df_quadtree, 12)

    context = {'img_list': list_img_ini}
    template = loader.get_template('moda/moreImages.html')
    return HttpResponse(template.render(context, request))
