from django.shortcuts import render
from .models import Owner, Sharer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.

def UserHome(request):
    return render(request, 'user/UserHome.html')

def UserOrder(request):
    return render(request, 'user/UserOrder.html')

def DriverRegister(request):
    return render(request, 'user/DriverRegister.html')

class Owner_InfoForm(LoginRequiredMixin, CreateView):
    model = Owner
    fields = ['Destination_Address',
              'Arrival_Date_Time',
              'Number_of_Passenger',
              'Vehicle_Type',
              'Special_Request',
              'Share_Or_Not',
              'max_share_num']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class Sharer_InfoForm(LoginRequiredMixin, CreateView):
    model = Sharer
    fields = ['Destination_Address',
              'Earliest_Arrival_Time',
              'Latest_Arrival_Time',
              'Number_of_Passenger',
              ]

    def form_valid(self, form):
        form.instance.sharer = self.request.user
        return super().form_valid(form)