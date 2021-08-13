from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import django_tables2 as tables
from .tables import PersonTable

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


class SimpleTable(tables.Table):
    class Meta:
        model = Funds2
class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Funds2.objects.all()
    template_name = "data_presentation/simple_template.html"

class PersonListView(tables.SingleTableView):

    model = Funds2
    table_class = PersonTable
    template_name = 'data_presentation/simple_template.html'

def home(request):
	context = {

		'categories':Funds.objects.all()

	}

	return render(request,'data_presentation/data_category.html',context)
