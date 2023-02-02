from django.shortcuts import render, redirect
from .models import Owner, Sharer, Driver
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.models import User


# Create your views here.

def UserHome(request):
    driver = Driver.objects.filter(driver=request.user.id).first()
    if driver is None:
        context = {'identity': 'rider'}
    else:
        context = {'identity': 'driver'}
    return render(request, 'user/UserHome.html', context)


# Owner

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


class OwnerEditRequest(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        if self.request.user == self.get_object().owner:
            return True
        return False


class OwnerDeleteRequest(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Owner
    success_url = '/user/owner/history/'

    def test_func(self):
        if self.request.user == self.get_object().owner:
            return True
        return False


# Sharer

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


# Driver

class Driver_InfoForm(LoginRequiredMixin, CreateView):
    template_name = 'user/driverregister_form.html'
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


class DriverSearchListView(ListView):
    template_name = 'user/driversearch_list.html'

    def get_queryset(self):
        return Owner.objects.filter(Status='open',
                                    Number_of_Passenger__lte=self.request.user.driver_set.last().Vehicle_Capacity,
                                    Vehicle_Type__in=['N/A', self.request.user.driver_set.last().Vehicle_Type],
                                    Special_Request__in=['N/A',
                                                         self.request.user.driver_set.last().Special_Information],
                                    ).exclude(
            owner=self.request.user).order_by('Arrival_Date_Time')


def DriverConfirm(request, rid):
    driver = Driver.objects.filter(user=request.user.id).first()
    ride = Owner.objects.filter(pk=rid).first()
    ride.Status = 'ongoing'
    ride.Driver_Name = request.user.username
    ride.Driver_License = driver.Driver_License
    ride.save()

    return render(request, 'user/UserHome.html')


class DriverProcessingListView(ListView):
    template_name = 'user/driverprocessing_list.html'

    def get_queryset(self):
        return Owner.objects.filter(Status='ongoing',
                                    Driver_Name=self.request.user.username).exclude(owner=self.request.user).order_by(
            'Arrival_Date_Time')


def DriverComplete(request, rid):
    ride = Owner.objects.filter(pk=rid).first()
    ride.status = 'complete'
    ride.save()
    return render(request, 'user/UserHome.html')
