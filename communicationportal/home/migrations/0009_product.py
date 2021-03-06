# Generated by Django 3.1.1 on 2020-09-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=None)),
                ('image', models.ImageField(blank=True, upload_to='products')),
            ],
        ),
    ]
