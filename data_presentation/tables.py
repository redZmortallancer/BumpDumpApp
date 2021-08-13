# tutorial/tables.py
import django_tables2 as tables
from .models import *

class PersonTable(tables.Table):
    class Meta:
        model = Funds2
        template_name = "django_tables2/bootstrap.html"