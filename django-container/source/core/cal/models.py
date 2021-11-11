from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import util


class Client(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=64)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    background_colour = models.CharField(max_length=7, default="#0d6efd")
    text_colour = models.CharField(max_length=7, default="#ffffff")

    def __str__(self):
        return f"{self.name} ({self.client.__str__()})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    clients = models.ManyToManyField(Client, blank=True)

    def get_username(self):
        return self.user.get_username()

    def get_short_name(self):
        return self.first_name if self.first_name else self.get_username()

    def get_name(self):
        return ' '.join([self.first_name, self.last_name]) if self.last_name else self.get_short_name()

    def __str__(self):
        return self.get_name()


class Booking(models.Model):
    resource = models.ForeignKey('Profile', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    notes = models.TextField(max_length=1000, blank=True)
    start = models.DateField()
    end = models.DateField()
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.pk}] {self.resource.get_name()}: {self.project.name}"
    
    def days_booked(self):
        """
        Takes booking object and outputs a string of comma separated days
        """

        if self.monday and self.tuesday and self.wednesday and self.thursday and self.friday and self.saturday and self.sunday:
            return "Every day"
        elif self.monday and self.tuesday and self.wednesday and self.thursday and self.friday:
            return "Week days only"
        elif self.saturday and self.sunday:
            return "Weekend days only"
        else:
            days = []
            if self.monday: days.append("Monday")
            if self.tuesday: days.append("Tuesday")
            if self.wednesday: days.append("Wednesday")
            if self.thursday: days.append("Thursday")
            if self.friday: days.append("Friday")
            if self.saturday: days.append("Saturday")
            if self.sunday: days.append("Sunday")
            if days == []:
                return "No days"
            return 'Every ' + ', '.join(days)
            