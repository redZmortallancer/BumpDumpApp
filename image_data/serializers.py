from rest_framework import serializers
from .models import FirstDaset,annotations


class annotationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = annotations
        fields = ['category_id', 'category_name', 'super_category_name','bounding_box','segmentaions','iscrowd']
          

class FirstDasetSerializer(serializers.ModelSerializer):
    annotations = annotationsSerializer(many=True, read_only=True)

    class Meta:
        model = FirstDaset
        fields = ['id','image_id', 'image_file_name', 'annotations']

