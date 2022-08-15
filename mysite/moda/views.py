from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



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

    context = {'img_list': list_img_ini}
    template = loader.get_template('moda/moreImages.html')
    return HttpResponse(template.render(context, request))
