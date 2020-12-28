from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.home),
    url(r'^1/',views.data),
    url(r'^login/',views.login),    
    url(r'^monitor/',views.monitor),    
    url(r'^search1/',views.search),    
]