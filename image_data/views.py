
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import pagination, generics, status
from .serializers  import FirstDasetSerializer  
from .models import FirstDaset,annotations
from django.db.models import Q
from django.shortcuts import render

from django.core import serializers


categories = annotations.objects.values('category_name').distinct()
print (categories)
dataset = annotations.objects.all()
print(len(dataset))

def dashboard_with_pivot(request):
    return render(request, 'image_data/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = annotations.objects.all()
    print(dataset.count)
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


class FirstDasetApiView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):

        if request.GET.get('category_name'):
            category_name = request.GET.get('category_name')
            FirstDasets = FirstDaset.objects.filter(Q(annotations__category_name=category_name))
        else:
            FirstDasets = FirstDaset.objects.all()
        paginator = pagination.PageNumberPagination()
        result_page = paginator.paginate_queryset(FirstDasets,request)

        if result_page is not None:
            serializer = FirstDasetSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = FirstDasetSerializer(result_page, many=True)
        print (request)
        print("done")
        return Response(serializer.data)

class FirstDasetDownload(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):

        if request.GET.get('category_name'):
            category_name = request.GET.get('category_name')
            FirstDasets = FirstDaset.objects.filter(Q(annotations__category_name=category_name))
        else:
            FirstDasets = FirstDaset.objects.all()

        if request.GET.get('lower_range') and request.GET.get('upper_range'):
            lower_range = request.GET.get('lower_range')
            upper_range = request.GET.get('upper_range')
            print(f'{lower_range}{upper_range}')
            FirstDasets = FirstDasets.filter(Q(id__gte=lower_range) & Q(id__lte=upper_range))

        '''paginator = pagination.PageNumberPagination()
        result_page = paginator.paginate_queryset(FirstDasets,request)

        if result_page is not None:
            serializer = FirstDasetSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        '''
        serializer = FirstDasetSerializer(FirstDasets, many=True)
        print (request)
        print("done")
        return Response(serializer.data)


class justincase(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):

        if request.GET.get('category_name'):
            category_name = request.GET.get('category_name')
            FirstDasets = FirstDaset.objects.filter(Q(annotations__category_name=category_name))
        else:
            FirstDasets = FirstDaset.objects.all()
        paginator = pagination.PageNumberPagination()
        result_page = paginator.paginate_queryset(FirstDasets,request)

        if result_page is not None:
            serializer = FirstDasetSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = FirstDasetSerializer(result_page, many=True)
        print (request)
        print("done")
        return Response(serializer.data)


class FirstDasetDetailView(ListView):

    
    model = FirstDaset
    template_name  = 'image_data/FirstDatasetDetail.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['annotainos'] = annotations.objects.all()
        context['categories'] = categories
        print("hey")
        return context
