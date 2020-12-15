from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30,default='')
    comment = models.TextField(default='')
    blog = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=60,default='')
    content = models.TextField(default='')
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogs/', blank=True)

    def __str__(self):
        return self.title
