from django.shortcuts import render, redirect
from .models import Owner, Sharer, Driver
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.models import User
from django.core.mail import send_mail


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


class SharerSearchListView(ListView):
    template_name = 'user/sharersearch_list.html'

    def get_queryset(self):
        return Owner.objects.filter(Share_Or_Not=True,
                                    Status='open',
                                    Destination_Address=self.request.user.sharer_set.last().Destination_Address,
                                    Arrival_Date_Time__gte=self.request.user.sharer_set.last().Earliest_Arrival_Time,
                                    Arrival_Date_Time__lte=self.request.user.sharer_set.last().Latest_Arrival_Time,
                                    Max_Share_Num__gte=self.request.user.sharer_set.last().Number_of_Passenger,
                                    ).exclude(
            owner=self.request.user).order_by('Arrival_Date_Time')


class SharerListView(ListView):
    template_name = 'user/sharer_list.html'

    def get_queryset(self):
        return Owner.objects.filter(Sharers_Name=self.request.user.username
                                    ).exclude(
            owner=self.request.user).exclude(Status='complete').order_by('Arrival_Date_Time')


def join(request, rid):
    ride = Owner.objects.filter(pk=rid).first()
    rideSharer = Sharer.objects.filter(sharer=request.user.id).last()
    ride.Status = 'open'
    ride.Sharers_Name = request.user.username
    ride.Number_of_Passenger = ride.Number_of_Passenger + rideSharer.Number_of_Passenger
    ride.save()
    return render(request, 'user/UserHome.html', {'identity': 'driver'})

class SharerEditRequest(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sharer
    fields = ['Destination_Address',
              'Earliest_Arrival_Time',
              'Latest_Arrival_Time',
              'Number_of_Passenger',
              ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().owner:
            return True
        return False

class SharerDeleteRequest(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sharer
    success_url = '/user/sharer/history/'

    def test_func(self):
        if self.request.user == self.get_object().owner:
            return True
        return False


# Driver
class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['Driver_Name',
                  'Vehicle_Type',
                  'Driver_License',
                  'Vehicle_Capacity',
                  'Special_Information',
                  ]


def driver_info(request):
    if request.method == 'POST':
        form = DriverUpdateForm(request.POST, instance=request.user.driver_set.last())
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('UserHome')

    else:
        form = DriverUpdateForm(instance=request.user.driver_set.last())

    context = {
        'form': form
    }

    return render(request, 'user/driverregister_form.html', context)


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
    driver = Driver.objects.filter(driver=request.user.id).first()
    ride = Owner.objects.filter(pk=rid).first()
    ride.Status = 'ongoing'
    ride.Driver_Name = request.user.username
    ride.Driver_License = driver.Driver_License
    ride.save()
    send_mail(
        'Riding_Sharing_Service Order Warnning',
        'Your order has been confirmed by a driver!',
        'zjy1298892386@gmail.com',
        ['' + ride.owner.email],
        fail_silently=False,
    )
    return render(request, 'user/UserHome.html', {'identity': 'driver'})


class DriverProcessingListView(ListView):
    template_name = 'user/driverprocessing_list.html'

    def get_queryset(self):
        return Owner.objects.filter(Status='ongoing',
                                    Driver_Name=self.request.user.username).exclude(owner=self.request.user).order_by(
            'Arrival_Date_Time')


def DriverComplete(request, rid):
    ride = Owner.objects.filter(pk=rid).first()
    ride.Status = 'complete'
    ride.save()
    return render(request, 'user/UserHome.html', {'identity': 'driver'})


class DriverListView(ListView):
    template_name = 'user/driver_list.html'

    def get_queryset(self):
        return Owner.objects.filter(Status='complete',
                                    Driver_License=self.request.user.driver_set.last().Driver_License,
                                   ).exclude(
            owner=self.request.user).order_by('Arrival_Date_Time')
