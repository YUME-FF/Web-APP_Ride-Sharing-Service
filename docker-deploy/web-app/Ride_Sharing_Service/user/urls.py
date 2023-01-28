from django.urls import path

from . import views
from .views import Owner_InfoForm
urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('owner/', Owner_InfoForm.as_view(), name='Owner'),
    path('share/', views.Sharer, name='Sharer'),
    path('history/', views.UserOrder, name='UserOrder'),
    path('driverregister/', views.DriverRegister, name='DriverRegister'),
]
