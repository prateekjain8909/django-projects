from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30,default='')
    address = models.CharField(max_length=100,default='')
    email = models.EmailField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    # time = models.DateTimeField(auto_now_add=True)
    # chat = models.FilePathField(path="/portal/media/chat/user2.py",default="hello")
    # models.DateTimeField()
    def __str__(self):
        return self.user.username

class Chat(models.Model):
    # sender = models.OneToOneField(User,on_delete=models.CASCADE)
    sender = models.CharField(max_length=30, default='')
    reciever = models.CharField(max_length=30, default='')
    logged_user = models.CharField(max_length=30, default='')
    time = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=1000 ,default="")

    def __str__(self):
        return self.sender+" to "+ self.reciever
class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class Product(models.Model):
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=None)
    image = models.ImageField(upload_to='products/',  null=True, verbose_name="")

    def __str__(self):
        return self.name

class RealEstate(models.Model):
    name= models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=None)
    image = models.ImageField(upload_to='realestate/',  null=True, verbose_name="")

    def __str__(self):
        return self.name

class Legal(models.Model):
    description = models.CharField(max_length=1000000)

    def __str__(self):
        return str("Legal")

def create_profile(sender, **kwags):
    if kwags['created']:
        Member.objects.create(user=kwags['instance'])




post_save.connect(create_profile, sender=User)

# def create_chat(sender, **kwags):
#     if kwags['created']:
#         Chat.objects.create(user=kwags['instance'])

# post_save.connect(create_chat, sender=User)
