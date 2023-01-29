from django.shortcuts import render
from .models import Owner, Sharer, Driver
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.

def UserHome(request):
    return render(request, 'user/UserHome.html')

# def DriverRegister(request):
#     driver = Driver()
#     # driver.
#     return render(request, 'user/DriverRegister.html')

class Driver_InfoForm(LoginRequiredMixin, CreateView): 
    model = Driver
    fields = ['Driver_Name',
              'Vehicle_Type',
              'Driver_License',
              'Vehicle_Capacity',
              'Special_Information',
              ]

    def form_valid(self, form):
        form.instance.driver = self.request.user
        return super().form_valid(form)

class Owner_InfoForm(LoginRequiredMixin, CreateView):
    model = Owner
    fields = ['Destination_Address',
              'Arrival_Date_Time',
              'Number_of_Passenger',
              'Vehicle_Type',
              'Special_Request',
              'Share_Or_Not',
              'Max_Share_Num']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerListView(ListView):
    template_name = 'user/owner_list.html'
    def get_queryset(self):
        return Owner.objects.filter(owner=self.request.user).order_by('Arrival_Date_Time')


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
