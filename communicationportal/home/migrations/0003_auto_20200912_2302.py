# Generated by Django 3.1 on 2020-09-12 23:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20200912_2300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chat1',
            new_name='Chat',
        ),
    ]
