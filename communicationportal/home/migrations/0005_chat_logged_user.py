# Generated by Django 3.1 on 2020-09-13 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200912_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='logged_user',
            field=models.CharField(default='', max_length=30),
        ),
    ]
