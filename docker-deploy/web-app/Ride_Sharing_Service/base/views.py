from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def logout(request):
    return render(request, 'logout.html')
def profile(request):
    return render(request, 'profile.html')
def createAccount(request):
    return render(request, 'createAccount.html')