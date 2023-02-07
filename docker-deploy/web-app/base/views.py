from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.forms import EmailField
from .models import User
rooms = [
    {'id': 1, 'name': 'Lets python'},
    {'id': 2, 'name': 'Lets Django'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('UserHome')
        else:
            messages.error(request, 'Username or passowrd is not correct')
    return render(request, 'base/login.html', {'page': 'login'})


def logout(request):
    django_logout(request)
    return redirect('home')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',
                  'email']

def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')

    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'base/profile.html', context)


class UserCreationForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
def createAccount(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            django_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please enter correct format')
    return render(request, 'base/login.html', {'form': form})

