from django.shortcuts import render
from .models import OwnerForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.

def UserHome(request):
    return render(request, 'user/UserHome.html')

def Owner(request):
    return render(request, 'user/Owner.html')

def Sharer(request):
    return render(request, 'user/Sharer.html')

def UserOrder(request):
    return render(request, 'user/UserOrder.html')

def DriverRegister(request):
    return render(request, 'user/DriverRegister.html')

class Owner_InfoForm(LoginRequiredMixin, CreateView):
    model = OwnerForm
    fields = ['Destination_Address',
              'Arrial_Date_Time',
              'Number_of_Passenger',
              'Vehicle_Type',
              'Special_Request',
              'Share_Or_Not',
              'max_share_num']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
