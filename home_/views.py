from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import django_tables2 as tables

from django_tables2 import SingleTableView





earlyContent = [

		{
			'name' :'tabular Data',

		},
		{
			'name' :'text Data',
		},
		{
			'name' :'imaga Data',
		},
		{
			'name' :'video Data',
		}


]



def homeOfSite(request):
	context = {

		'categories':earlyContent

	}

	return render(request,'home_/home.html',context)
