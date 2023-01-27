from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('createAccount/',views.createAccount, name='createAccount'),
    path('driverRegister/',views.driverRegister,name='driverRegister')
]
