from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
rooms = [
    {'id':1, 'name':'Lets python'},
    {'id':2, 'name':'Lets Django'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User does not exist!')
    return render(request, 'base/login.html')
def logout(request):
    return render(request, 'base/logout.html')
def profile(request):
    return render(request, 'base/profile.html')
def createAccount(request):
    return render(request, 'base/createAccount.html')
def driverRegister(request):
    return render(request, 'base/driverRegister.html')