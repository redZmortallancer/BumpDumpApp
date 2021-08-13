
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import FirstDaset,annotations

from django.http import JsonResponse
from django.shortcuts import render

from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'image_data/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = annotations.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

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
        return context
