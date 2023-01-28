from django.urls import path

from . import views
from .views import Owner_InfoForm, Sharer_InfoForm
urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('owner/', Owner_InfoForm.as_view(), name='Owner'),
    path('share/', Sharer_InfoForm.as_view(), name='Sharer'),
    path('history/', views.UserOrder, name='UserOrder'),
    path('driverregister/', views.DriverRegister, name='DriverRegister'),
]
