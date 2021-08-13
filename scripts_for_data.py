import os, sys
sys.path.append('')
os.environ['DJANGO_SETTINGS_MODULE'] = 'data_share.settings'
import django
import json
django.setup()
from django.contrib.auth.models import User

with open("instances_val2017.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
for row in data:
    user = User.objects.create_user(username=row['username'])