from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
import re
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = models.Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    args = {"blogs": blogs}
    return render(request, "home.html",args)

@login_required(login_url='/admin')
def add(request):
    print(str(request))
    print(str(request.session))
    if request.method == 'POST':
        blog = forms.BlogForm(request.POST, request.FILES)
        blog.save()
        return HttpResponseRedirect("/")
    return render(request, "add.html")

def detail(request):
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']
        cmmnt = models.Comment()
        cmmnt.name = name
        cmmnt.comment = comment
        cmmnt.save()
    return render(request, "post.html")


def blog_details(request, pk=None):
    blog_id = str(request)
    blog_id = re.findall(".+([0-9]+)", blog_id)[0]
    blog = models.Blog.objects.filter(id=blog_id)[0]
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']
        cmmnt = models.Comment()
        cmmnt.name = name
        cmmnt.comment = comment
        cmmnt.blog = blog_id
        cmmnt.save()
        return HttpResponseRedirect("/blog/{}".format(blog_id))
        
    comments = models.Comment.objects.filter(blog=blog_id)
    comments.order_by("time")
    # print(blog)
    args = {"blog" : blog, "comments":reversed(comments)}
    return render(request, "blog_details.html",args)
        

@login_required(login_url='/admin')
def edit_blog(request, pk=None):
    blog_id = str(request)
    blog_id = re.findall(".+([0-9]+)", blog_id)[0]
    blog = models.Blog.objects.filter(id=blog_id)[0]
    if request.method == 'POST':
        blog = forms.BlogForm(request.POST, request.FILES,instance=blog)
        blog.save()
        return HttpResponseRedirect("/blog/{}".format(blog_id))
    # print(blog)
    args = {"blog" : blog}
    return render(request, "edit_blog.html",args)
    # return render(request, "add.html")