from django.urls import path

from . import views
from .views import Owner_InfoForm, Sharer_InfoForm, OwnerListView, Driver_InfoForm, DriverListView
urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('owner/', Owner_InfoForm.as_view(), name='Owner'),
    path('owner/history/', OwnerListView.as_view(), name='OwnerListView'),
    path('share/', Sharer_InfoForm.as_view(), name='Sharer'),
    path('driverRegister/',Driver_InfoForm.as_view() , name='DriverRegister'),
    path('driverSelect/',DriverListView.as_view() , name='DriverSelect'),
    path('driverSelect/driverOnProcess/',views.DriverOnProcess , name='DriverOnProcess'),

]
