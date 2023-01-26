from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the home.")
def logIn(request):
    return HttpResponse("This is Log in page")
def logOut(request):
    return HttpResponse("This is Log out page")
def profile(request):
    return HttpResponse("This is profile page")
def createAccount(request):
    return HttpResponse("This is create account page")