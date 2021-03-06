# Generated by Django 3.1.2 on 2021-08-28 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstDaset',
            fields=[
                ('id', models.IntegerField(primary_key='True', serialize=False)),
                ('image_id', models.CharField(max_length=100)),
                ('image_file_name', models.CharField(max_length=100)),
                ('coco_Url', models.CharField(max_length=100)),
                ('flicker_Url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='annotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('super_category_name', models.CharField(default='default string', max_length=100)),
                ('bounding_box', models.CharField(default='default string', max_length=200)),
                ('segmentaions', models.CharField(default='default string', max_length=400)),
                ('iscrowd', models.CharField(max_length=20)),
                ('imageObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='image_data.firstdaset')),
            ],
        ),
    ]
