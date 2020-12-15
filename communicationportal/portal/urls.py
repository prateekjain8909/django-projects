from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def login_redirect(request):
    return redirect('/login')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"", include('home.urls')),    
    url(r"^$", login_redirect, name='login_redirect'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
