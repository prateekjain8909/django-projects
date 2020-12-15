# Generated by Django 3.1.3 on 2020-12-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
                ('content', models.TextField(default='')),
                ('time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='blogs/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('comment', models.TextField(default='')),
                ('blog', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]