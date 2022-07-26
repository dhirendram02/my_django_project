from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from info import settings

# Create your views here.
def home(request):
    return render(request, "EmpInfo/index.html")

def signup(request):
    if request.method == "POST":
        username =request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exit! Please try some other ")
            return redirect('home')

        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")

       
        
        if not username.isalnum():
            messages.error(request, "Username must be alpha numeric!")
            return redirect('home')

            
        
        myuser = User.objects.create_user(username, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account has been successfully created. ")
        
        return redirect('signin')

     
    return render(request, "EmpInfo/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
        else:
            
            return redirect('home')

    return render(request, "EmpInfo/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')
