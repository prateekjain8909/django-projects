# Generated by Django 3.1 on 2020-09-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200913_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image/'),
        ),
    ]
