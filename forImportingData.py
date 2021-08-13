
import django
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'data_share.settings'
django.setup()

import json
from django.core.files.base import ContentFile, File
from image_data.models import FirstDaset,annotations

FirstDaset.objects.all().delete()
annotations.objects.all().delete()


with open("TESTINGDATA/annotations/instances_val2017.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

    categoires = {}

    for k in range(len(jsonObject['categories'])): 
        categoires[jsonObject['categories'][k]['id']] = k

    print (categoires)
    print (categoires[1])
    for i in range(len(jsonObject['images'])):
        fileName = jsonObject['images'][i]['file_name']
        new_name = jsonObject['images'][i]['id']

        with open(f'TESTINGDATA/val2017/{fileName}','rb') as f:

            savedIDs = []
            

            for j in range(len(jsonObject['annotations'])): 
                
                if (new_name == jsonObject['annotations'][j]['image_id']):
                    savedIDs.append(j)
                   # print(f'{new_name} = {j}')


            #print(f'{new_name} =  {savedIDs}')
            
         #print(cat_id)
            firstDataset = FirstDaset(image_id =str(jsonObject['images'][i]['id']),
                image_file_name=fileName,
                
            )

            firstDataset.photo.save(f'{fileName}',File(f))
            firstDataset.save()
            
            for savedID in savedIDs:
                Annotations = annotations( imageObject = firstDataset,
                category_id = jsonObject['annotations'][savedID]['category_id'],
                category_name = jsonObject['categories'][categoires[jsonObject['annotations'][savedID]['category_id']]]['name'],
                super_category_name = jsonObject['categories'][categoires[jsonObject['annotations'][savedID]['category_id']]]['supercategory'],
                bounding_box =  jsonObject['annotations'][savedID]['bbox'],
                segmentaions =  jsonObject['annotations'][savedID]['segmentation']
            
                )
                Annotations.save()

           
