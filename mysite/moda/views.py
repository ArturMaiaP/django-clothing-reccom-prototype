from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .SelectImages import *
from .Constantes import *

# Create your views here.
select_images = SelectImages()


def index(request):
    template = loader.get_template('moda/index.html')
    return HttpResponse(template.render(None, request))


def init_gallery(request):

    list_img_ini = select_images.select_images_distance()
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

    if (len(list_rel) < TAMANHO_MINIMO_SVM) and (len(list_irrel) < TAMANHO_MINIMO_SVM):
        list_img_ini = select_images.select_images_distance()
    else:
        list_img_ini = select_images.select_images_svm(list_rel, list_irrel)

    context = {'img_list': list_img_ini}
    template = loader.get_template('moda/moreImages.html')
    return HttpResponse(template.render(context, request))
