from django.db import models
import json

# Create your models here.

class FirstDaset(models.Model):

    id =    models.IntegerField(primary_key = 'True')
    image_id = models.CharField(max_length=100)
    image_file_name = models.CharField(max_length=100)
    coco_Url = models.CharField( max_length=100)
    flicker_Url = models.CharField( max_length=100)

    def get_categories(self):
        return self.annotations.all()
    def get_categories_count(self):
        return self.annotations.count()

class annotations(models.Model):
        imageObject = models.ForeignKey(
            FirstDaset, on_delete=models.CASCADE, related_name='annotations')
        category_id = models.CharField(max_length=100)
        category_name = models.CharField(max_length=100)
        super_category_name =  models.CharField(max_length=100,default='default string') 
        bounding_box = models.CharField(max_length=200,default='default string') 
        segmentaions = models.CharField(max_length=400,default='default string') 
        iscrowd = models.CharField(max_length=20)

        def set_bounding_box(self, x):
            self.foo = json.dumps(x)

        def get_bounding_box(self):
            return json.loads(self.foo)

        def set_segmentaions(self, x):
            self.foo = json.dumps(x)

        def get_segmentaions(self):
            return json.loads(self.foo)
        
        