from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

TYPE_CHOICES = (
    ("SUV", "SUV"),
    ("COMPACT", "COMPACT"),
    ("SEDAN", "SEDAN"),
    ("COUPE", "COUPE"),
    ("--", "--"),
)


class Owner(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Form should be filled by owner requesting for a ride
    Destination_Address = models.CharField(max_length=100)
    Arrival_Date_Time = models.DateTimeField(help_text='Format: 2020-01-01 12:00')
    Number_of_Passenger = models.PositiveIntegerField(default=1)
    Vehicle_Type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='--')
    Special_Request = models.CharField(max_length=400, blank=True)
    Share_Or_Not = models.BooleanField()
    Max_Share_Num = models.PositiveIntegerField(help_text='If you do not want to share please choose 0', default=0)

    # open: driver not confirmed; (can be cancelled by owner)
    # ongoing: driver confirmed;
    # completed: driver confirmed;
    Status = models.CharField(default='open', max_length=20)
    Sharers_Name = models.CharField(default='', max_length=50, blank=True)

    Driver_Name = models.CharField(default='', max_length=50, blank=True)
    Driver_License = models.CharField(default='', max_length=50, blank=True)

    def __str__(self):
        return self.Destination_Address

    # Submit --> View ride Status
    def get_absolute_url(self):
        return reverse('OwnerListView')


class Sharer(models.Model):
    sharer = models.ForeignKey(User, on_delete=models.CASCADE)
    # Form should be filled by sharer searching for a ride
    Destination_Address = models.CharField(max_length=100)
    Earliest_Arrival_Time = models.DateTimeField(help_text='Format: 2020-01-01 12:00')
    Latest_Arrival_Time = models.DateTimeField(help_text='Format: 2020-01-01 13:00')
    Number_of_Passenger = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Destination_Address

    # Submit --> View ride Status
    def get_absolute_url(self):
        return reverse('SharerSearchListView')


class Driver(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    Driver_Name = models.CharField(max_length=20)
    Vehicle_Type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='N/A')
    Driver_License = models.CharField(default='', max_length=50)
    Vehicle_Capacity = models.PositiveIntegerField(default=1)
    Special_Information = models.CharField(default='N/A', max_length=100, blank=True)

    def __str__(self):
        return self.Driver_Name

    # Submit --> View  UserHome
    def get_absolute_url(self):
        return reverse('UserHome')
