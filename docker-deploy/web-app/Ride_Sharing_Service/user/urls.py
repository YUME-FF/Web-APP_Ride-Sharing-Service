from django.urls import path

from . import views
from .views import Owner_InfoForm, Sharer_InfoForm, OwnerListView
urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('owner/', Owner_InfoForm.as_view(), name='Owner'),
    path('owner/history/', OwnerListView.as_view(), name='OwnerListView'),
    path('share/', Sharer_InfoForm.as_view(), name='Sharer'),
    path('driverregister/', views.DriverRegister, name='DriverRegister'),
]
