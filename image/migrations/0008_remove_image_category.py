# Generated by Django 3.0 on 2019-12-16 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_remove_image_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
    ]
