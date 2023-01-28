from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
rooms = [
    {'id':1, 'name':'Lets python'},
    {'id':2, 'name':'Lets Django'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms':rooms}) 

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password = password)
        if user is not None:
            django_login(request, user)
            return redirect('UserHome')
        else:
            messages.error(request, 'Username or passowrd is not correct')
    return render(request, 'base/login.html', {'page':'login'})

def logout(request):
    django_logout(request)
    return redirect('home')


def profile(request):
    return render(request, 'base/profile.html')
def createAccount(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            django_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct format')
    return render(request, 'base/login.html',{'form':form})
def driverRegister(request):
    return render(request, 'base/driverRegister.html')