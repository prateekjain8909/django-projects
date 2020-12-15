
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'add/', views.add),
    url(r'detail/', views.detail),
    url(r"blog/([0-9]+)/$", views.blog_details),
    url(r"blog/([0-9]+)/edit$", views.edit_blog),
]