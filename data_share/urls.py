"""data_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from data_presentation.views import *
from home_ import views as home_views
from image_data import views as data_share_views
from image_data import api as data_share_apis

from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    path('', home_views.homeOfSite, name = 'home'),
    path('admin/', admin.site.urls),
    path('projects/', PersonListView.as_view(),name = 'tabluar'),
    path('data/', include('data_presentation.urls')),
    path('images/', data_share_views.FirstDasetDetailView.as_view(), name = 'image_data'),
    path('dashboard/', data_share_views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('dashboard/data', data_share_views.pivot_data, name='pivot_data'),
    path('images/api/search/',data_share_apis.api_search, name = 'image_search'),
    path('images/api/', data_share_views.FirstDasetApiView.as_view(),name = 'image_api'),
    path('images/api/download/', data_share_views.FirstDasetDownload.as_view(),name = 'image_api_download')

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

