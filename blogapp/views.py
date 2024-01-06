from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from . models import UserDetails
from .form import Blogform
from . models import blogmodel
from django.contrib.auth.decorators import login_required
from . import urls
from django.urls import reverse

# Create your views here.
def home(request):
    blog = blogmodel.objects.all().order_by('-created_at')
    return render(request,'blogapp/home.html',{'blog':blog})

def register(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        number = request.POST.get('number')
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username Taken By another")
            return redirect('/register/')

        user = User.objects.get_or_create(
            username = username,
            password = make_password(str(password)),
        )
        details = UserDetails.objects.get_or_create(
            name = name,
            number = number,
            email = email,
            Username = username,
        )
        messages.info(request,'Accounts Created SuccessFully')
        # return HttpResponse('<h1>User Created Sucessfully</h1> <a href="/">Home</a>') 
    return render(request,'registration/register.html')

@login_required
def logout_user(request):
    try:
        if request.method =='GET':
            logout(request)
            messages.success(request,'Successfully Logout')
            return redirect('/')
    except Exception as e:
        print(e)
        return messages.success(request,'There was some error to do logout please login again')
    
@login_required
def add_blog(request):
    form = Blogform
    try:
        if request.method == "POST":
            form = Blogform(request.POST)
            title = request.POST.get('title')
            image = request.FILES['image']
            user = request.user
            # print(image)
            if form.is_valid():
                content = form.cleaned_data['content']
            blogmodel.objects.create(
                user = user,title = title,image = image,content = content,
            )
            messages.success(request,'Added blog SuccessFully')
            return redirect('/')
        else:
            redirect ('/')
            

    except Exception as e:
        print('error',e)
    
    return render(request,'blogapp/add_blog.html',{'form':form})

def blog_detail(request,slug):
    blog_obj = blogmodel.objects.filter(slug = slug)
    return render(request,'blogapp/blog_detail.html',{'blog_obj':blog_obj})

@login_required
def see_blog(request):
    try:
         blog_objs = blogmodel.objects.filter(user = request.user)

    except Exception as e:
        print(e)


    return render(request,'blogapp/see_blog.html',{'blog_objs':blog_objs})

def blog_delete(request,id):
    try:
        blog_objd = blogmodel.objects.get(id=id)
        if blog_objd.user == request.user:
            blog_objd.delete()
    except Exception as e:
        print(e)
    messages.success(request,'Post is Deleted')
    return redirect('/see-blog')

def blog_update(request, slug):
    try:
        blog_obj = blogmodel.objects.get(slug=slug)
        if blog_obj.user != request.user:
            return redirect('/')
        
        if request.method == 'POST':
            form = Blogform(request.POST,instance=blog_obj)
            if form.is_valid():
                form.save()
                return redirect('/see-blog')
        else:
            form = Blogform(instance=blog_obj)

    except Exception as e:
        print(e)
    return render(request,'blogapp/update_blog.html',{'form':form})

