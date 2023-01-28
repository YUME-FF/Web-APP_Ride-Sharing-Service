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

class OwnerForm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #Form should be filled by owner requesting for a ride
    Destination_Address = models.CharField(max_length=100)
    Arrial_Date_Time = models.DateTimeField(help_text='Format: 2020-01-01 12:00')
    Number_of_Passenger = models.PositiveIntegerField(default=1)
    Vehicle_Type =models.CharField(max_length=20, choices=TYPE_CHOICES, default='--')
    Special_Request = models.CharField(max_length=400, blank=True)
    Share_Or_Not = models.BooleanField()
    max_share_num = models.PositiveIntegerField(help_text='If you do not want to share please choose 0', default=0)

    def __str__(self):
        return self.owner
