from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .form import RegistrationForm,EditProfileForm,VideoForm,ProductForm,RealEstateForm,LegalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
import datetime
from .models import Chat,Member,Video,Product,RealEstate,Legal
from .login_check import logged_user
import re
from django.core.paginator import Paginator

# from .models import 

# @user_passes_test(redirect_field_name='/home')
def login(request):
    return HttpResponseRedirect("/login")

@login_required(login_url='/login')
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='/login')
def chat_view(request):

    objects = Member.objects.exclude(user_id=request.user.id)
    # admin = Member.objects.filter(id=5)
    # objects = objects.difference(admin)
    if objects:
        obj_ins = objects[0]
    else:
        obj_ins = None

    if request.user.username != "admin":
        chat_objects1 = Chat.objects.filter(sender=request.user, reciever="admin")
        chat_objects2 = Chat.objects.filter(sender="admin", reciever=request.user)
        chat_objects =  (chat_objects1.union(chat_objects2))
        chat_object = logged_user(chat_objects, request.user.username)
        if request.method == "POST":
            
            chat = Chat()
            chat.sender = request.user
            chat.message = request.POST["message"]
            chat.reciever = "admin"
            chat.save()
            chat_objects1 = Chat.objects.filter(sender=request.user, reciever="admin")
            chat_objects2 = Chat.objects.filter(sender="admin", reciever=request.user)
            chat_objects = chat_objects1.union(chat_objects2)
            chat_objects = (chat_objects.order_by("time"))
            chat_objects = logged_user(chat_objects, request.user.username)
            return HttpResponseRedirect("/profile/chat")
        return render(request, 'home/chat.html', {"data": reversed(chat_objects)})
    else:
        if request.method == "POST":
            try:
                reciever = request.POST["user_name"]
                request.session["reciever"] = reciever
                chat_objects1 = Chat.objects.filter(sender=request.user, reciever=reciever)
                chat_objects2 = Chat.objects.filter(sender=reciever, reciever=request.user)
                chat_objects = chat_objects1.union(chat_objects2)
                chat_objects = (chat_objects.order_by("time"))
                chat_objects = logged_user(chat_objects, request.user.username)
                obj_ins_id = User.objects.select_related("member").get(username=reciever)
                obj_ins = Member.objects.filter(user_id=obj_ins_id.id)[0]
                args = { "objects": objects, "data" : reversed(chat_objects), "obj_ins": obj_ins}
                return render(request, 'home/admin_chat.html', args)
            except Exception:
                message = request.POST['message']
                reciever = request.session["reciever"]
                print(reciever)
                chat = Chat()
                chat.sender = request.user
                chat.message = message
                chat.reciever = reciever
                chat.save()
                chat_objects1 = Chat.objects.filter(sender=request.user, reciever=reciever)
                chat_objects2 = Chat.objects.filter(sender=reciever, reciever=request.user)
                chat_objects = chat_objects1.union(chat_objects2)
                chat_objects = (chat_objects.order_by("time"))
                chat_objects = logged_user(chat_objects, request.user.username)
                obj_ins_id = User.objects.select_related("member").get(username=reciever)
                obj_ins = Member.objects.filter(user_id=obj_ins_id.id)[0]
                args = { "objects": objects, "data" : reversed(chat_objects), "obj_ins": obj_ins}
                return render(request, 'home/admin_chat.html', args )
        

        chat_objects1 = Chat.objects.filter(sender=request.user, reciever=obj_ins.user)
        chat_objects2 = Chat.objects.filter(sender=obj_ins.user, reciever=request.user)
        chat_objects =  (chat_objects1.union(chat_objects2))
        chat_object = logged_user(chat_objects, request.user.username)
        print(obj_ins.image.url)
        args = { "objects": objects, "data" : reversed(chat_objects), "obj_ins ": obj_ins}
        return render(request, 'home/admin_chat.html',args)
    
@login_required(login_url='/login')
def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    args = {"products": products}
    return render(request, 'home/products.html',args)

@login_required(login_url='/login')
def add_products(request):
    if request.user.username == "admin":
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        args = { "products": products }
        if request.method == "POST":
            for count, x in enumerate(request.FILES.getlist("image")):
                form= ProductForm(request.POST or None, {'image':x})
                if form.is_valid():
                    form.save()
            return HttpResponseRedirect("/products/add/")
        return render(request, 'add_products.html', args)
    else:
        return HttpResponseRedirect("/products/")

@login_required(login_url='/login')
def product_details(request, pk=None):
    try:
        product_id = str(request)
        product_id = re.findall(".+([0-9]+)", product_id)[0]
        product = Product.objects.filter(id=product_id)[0]
        print(product)
        args = {"product" : product}
        return render(request, "home/product_details.html",args)
    except Exception:
        return HttpResponseRedirect("/products/")

@login_required(login_url='/login')
def real_estate(request):
    real_estates = RealEstate.objects.all()
    args = {"real_estates": real_estates}
    return render(request, 'home/real_estate.html',args)

@login_required(login_url='/login')
def add_real_estate(request):
    if request.user.username == "admin":
        real_estates = RealEstate.objects.all()
        args = { "real_estates": real_estates }
        if request.method == "POST":
            form= RealEstateForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/real-estate/add/")
            else:
                return HttpResponseRedirect("/real-estate/add/")
        return render(request, 'home/add_real_estate.html', args)
    else:
        return HttpResponseRedirect("/real-estate/")

@login_required(login_url='/login')
def real_estate_details(request, pk=None):
    try:
        real_estate_id = str(request)
        real_estate_id = re.findall(".+([0-9]+)", real_estate_id)[0]
        real_estate = RealEstate.objects.filter(id=real_estate_id)[0]
        # print(real_estate)
        args = {"real_estate" : real_estate}
        return render(request, "home/real_estate_details.html",args)
    except Exception:
        return HttpResponseRedirect("/real-estate/")
    
@login_required(login_url='/login')
def videos(request):
    # print("videos")
    videos = Video.objects.all()
    paginator = Paginator(videos, 6)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    args = { "videos": videos }
    return render(request, 'home/videos.html', args)

@login_required(login_url='/login')
def add_videos(request):
    if request.user.username == "admin":
        videos = Video.objects.all()
        paginator = Paginator(videos, 5)
        page = request.GET.get('page')
        videos = paginator.get_page(page)
        args = { "videos": videos }
        if request.method == "POST":
            for count, x in enumerate(request.FILES.getlist("videofile")):
                form= VideoForm(request.POST or None, {'videofile':x})
                if form.is_valid():
                    form.save()
            return HttpResponseRedirect("/videos/add/")
        return render(request, 'add_videos.html', args)
    else:
        return HttpResponseRedirect("/videos/")
        
def register(request):
    if request.method == 'POST':
        full_name = str(request.POST['first_name']) + str(request.POST['last_name'])
        form = RegistrationForm(request.POST)
        form2 = EditProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid() and form2.is_valid():
            form.save()
            obj_ins_id = User.objects.select_related("member").get(username=request.POST['username'])
            obj_ins = Member.objects.filter(user_id=obj_ins_id.id)[0]
            obj_ins.full_name = full_name
            obj_ins.address = request.POST['address']
            obj_ins.email = request.POST['email']
            obj_ins.image = 'profile_image/'+request.POST['image']
            obj_ins.save()
            return redirect('/home')
        else:
            print(request.POST)
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'register.html', args)

@login_required(login_url='/login')
def view_profile(request):
    if request.method == 'POST':    
        return redirect('/logout')
    args = {'user':request.user}
    return render(request, 'home/view_profile.html',args)

@login_required(login_url='/login')
def edit_profile(request):
    if request.method == 'POST':
        # print(request.POST)
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.save()      

        obj_ins_id = User.objects.select_related("member").get(username=request.user.username)
        obj_ins = Member.objects.filter(user_id=obj_ins_id.id)[0]        
        obj_ins.address = request.POST['address']
        obj_ins.email = request.POST['email']
        obj_ins.phone = request.POST['phone']
        obj_ins.image = request.POST['image']
        obj_ins.save()
        # d = dict(request.POST)
        # d.update({'user_id': request.user.member.user_id})
        # print(d)
        # form = EditProfileForm(d or None, request.FILES or None,)
        # if form.is_valid():
        #     form.save()
        return redirect('/profile/')
    else:       
        form = EditProfileForm()
    args = {"form": form['image']}
    # print(type(request.user.member.user_id))
    return render(request,'home/edit_profile.html',args)

    
@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/profile')
        else:
            return redirect('/profile/change-password')

    else:
        form = PasswordChangeForm(user=request.user)        
        args = {'form': form}
        return render(request, 'home/change_password.html', args)
        
@login_required(login_url='/login')
def legal(request):
    legal = Legal.objects.all()
    if legal:
        args = {"legal": legal[0]}
        print(legal[0].description)
    else:
        args={}
    if request.method == "POST":
        legal = Legal.objects.all()
        if legal:
            legal[0].description = request.POST["description"]
            legal[0].save()
            return HttpResponseRedirect("/legal/")

        else:
            form = LegalForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/legal/")

    return render(request, 'legal.html', args)
    
@login_required(login_url='/login')
def category(request):
    return render(request, "category.html")

# @login_required(login_url='/login')
# def chat(request):
#     # message = ''
#     # user_name = request.user

#     if request.method == "POST":
#         # print(request.POST['message'])
#         # time = datetime.datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
#         # print(time)
#         # i = list(map(int, time.split(',')))
#         # message_time = datetime.datetime(i[0], i[1], i[2], i[3], i[4], i[5])
#         # message_time_formatted = message_time.strftime("%I:%M %p now")
#         # data.insert(0,{
#         #     "date":time,
#         #     "user":'user2',
#         #     "message": request.POST['message'],
#         #     'message_time_formatted': message_time_formatted,
#         # })from user2 import data
#         # request.user.member.chat.append("Hawfesafs")
#         # print(request.user.member.chat)
#         # message=request.POST['message']
#         # get_chat_data(message, user_name)
#         # for item in user2.data:
#         #     item['current_user'] = request.user.username
#         # refreshed_data = user2.data[:]
#         # refreshed_data.append({"date1":"2020,09,12,15,56,57","user":request.user.username,"message":message,'current_user':request.user.username})
#         # args = {'data': refreshed_data, 'user': request.user}

#         chat = Chat()
#         chat.user = request.user
#         chat.time = datetime.datetime.now()
#         chat.message = request.POST["message"]
#         chat.reciever = "admin"
#         return render(request, 'home/admin_chat.html',)
#     # get_chat_data(message, user_name)
#     # for item in user2.data:
#     #     item['current_user'] = request.user.username
#     # args = {'data': user2.data,'user':request.user}
#     return render(request, 'home/admin_chat.html',)