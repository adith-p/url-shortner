from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

from random import choice
import string
from .models import Urldata,User

# Create your views here.

def index(request):
    return render(request,'shortner/index.html')

def auth(request):
    return render()

@login_required(login_url='/login/')
def shortid(request):
    url_objs = Urldata.objects.filter(created_by=request.user)
    return render(request,'shortner/index.html',{'data':url_objs})

@login_required(login_url='/login/')
def redirect_url(request):
    if request.method == 'POST':
        short_id: str = request.POST.get('short_id')
        url_instance = get_object_or_404(Urldata,short_id=short_id.strip())
        return redirect(url_instance.original_url)
    return render(request,'shortner/redirect.html')

@login_required(login_url='/login/')
def add_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_id =''.join(choice(string.ascii_letters+string.digits) for _ in range(8))
        url_instance = Urldata.objects.create(original_url=original_url,created_by=request.user,short_id=short_id)
        url_instance.save()
    return redirect(shortid)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        

        if user:
            login(request,user)
            return redirect(index)
        
        return render(request, 'shortner/login.html', {
                "message": "Invalid username and/or password."
            })
    return render(request, "shortner/login.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            messages.add_message(request, messages.WARNING,"Username already taken.")
            return render(request, "shortner/auth.html")

        login(request,user)
        return redirect(index)
    return render(request, "shortner/signup.html")
    
@login_required(login_url='login/')
def logout_view(request):
    logout(request)
    return redirect(login_view)