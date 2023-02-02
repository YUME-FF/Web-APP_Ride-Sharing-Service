from django.urls import path

from . import views
from .views import Owner_InfoForm, OwnerListView, OwnerEditRequest, \
    OwnerDeleteRequest, Sharer_InfoForm, Driver_InfoForm, DriverSearchListView, DriverProcessingListView

urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('owner/', Owner_InfoForm.as_view(), name='Owner'),
    path('owner/history/', OwnerListView.as_view(), name='OwnerListView'),
    path('owner/history/<int:pk>/edit', OwnerEditRequest.as_view(), name='OwnerEditRequest'),
    path('owner/history/<int:pk>/delete', OwnerDeleteRequest.as_view(), name='OwnerDeleteRequest'),

    path('share/', Sharer_InfoForm.as_view(), name='Sharer'),

    path('driverRegister/', Driver_InfoForm.as_view(), name='DriverRegister'),
    path('driverSearchListView/', DriverSearchListView.as_view() , name='DriverSearchListView'),
    path('driverProcessingListView/', DriverProcessingListView.as_view() , name='DriverProcessingListView'),
    path('<int:rid>/driverconfirm', views.DriverConfirm , name='DriverConfirm'),
    path('<int:rid>/drivercomplete', views.DriverComplete , name='DriverComplete'),
]
