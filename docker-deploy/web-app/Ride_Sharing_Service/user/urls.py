from django.urls import path

from . import views
from .views import Owner_InfoForm, OwnerListView, OwnerEditRequest, OwnerDeleteRequest, \
    Sharer_InfoForm, SharerSearchListView, SharerListView, SharerDeleteRequest,\
    Driver_InfoForm, DriverSearchListView, DriverProcessingListView

urlpatterns = [
    path('', views.UserHome, name='UserHome'),
    path('owner/', Owner_InfoForm.as_view(), name='Owner'),
    path('owner/history/', OwnerListView.as_view(), name='OwnerListView'),
    path('owner/history/<int:pk>/edit', OwnerEditRequest.as_view(), name='OwnerEditRequest'),
    path('owner/history/<int:pk>/delete', OwnerDeleteRequest.as_view(), name='OwnerDeleteRequest'),

    path('sharer/', Sharer_InfoForm.as_view(), name='Sharer'),
    path('sharer/history/', SharerListView.as_view(), name='SharerListView'),
    path('sharer/history/<int:pk>/delete', SharerDeleteRequest.as_view(), name='SharerDeleteRequest'),
    path('sharer/SearchListView/', SharerSearchListView.as_view(), name='SharerSearchListView'),
    path('sharer/SearchListView/<int:rid>/join/', views.join, name='SharerJoin'),

    path('driverRegister/', Driver_InfoForm.as_view(), name='DriverRegister'),
    path('driverSearchListView/', DriverSearchListView.as_view() , name='DriverSearchListView'),
    path('driverProcessingListView/', DriverProcessingListView.as_view() , name='DriverProcessingListView'),
    path('<int:rid>/driverconfirm', views.DriverConfirm , name='DriverConfirm'),
    path('<int:rid>/drivercomplete', views.DriverComplete , name='DriverComplete'),
]
