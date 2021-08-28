import json
from django.core import paginator

from django.db.models import Q
from django.http import JsonResponse, HttpResponse

from .models import FirstDaset, annotations
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger









def api_search(request):
    imagelist = []

    data = json.loads(request.body)
    query = data['query']

    images = FirstDaset.objects.filter(Q(annotations__category_name=query))

    for image in images:
        annotationlist = []

        for annotation in image.annotations.all():
            annotate = {
                'category_name': annotation.category_name,
                'super_category_name': annotation.super_category_name

            }

            annotationlist.append(annotate)
        obj = {
            'id': image.image_id,
            'file_name': image.image_file_name,
            'annotations': annotationlist,

        }
        # print('next image ')
        # print((annotationlist))
        # print('\n')
        imagelist.append(obj)
        
    return JsonResponse({'images': imagelist})

'''    paginator = Paginator(imagelist, 25)

        page = request.GET.get('page')

        try:
            imagelistPage = paginator.page(page)
        except PageNotAnInteger:
            imagelistPage = paginator.page(1)
        except EmptyPage:
            imagelistPage = paginator.page(paginator.num_pages)'''
    #print (query)
    # print(imagelist[1])
    #data = serializers.serialize('json', imagelist)
    # return HttpResponse(data, content_type="application/json")
    
