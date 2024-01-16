from django.db import models

from django.contrib.auth.models import User

from datetime import time


class Location(models.Model):
    adress = models.CharField(max_length=100)
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.adress}, room {self.room_number}."


class Specialization(models.Model):
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.specialization


class Doctor(models.Model):
    doctor = models.CharField(max_length=50)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor} ({self.specialization})"


class Visit(models.Model):
    date = models.DateField()
    start_time = models.TimeField(default=time(8))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    patient = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date", "start_time"]

    def __str__(self):
        return f"{self.date} ({self.start_time}) - {self.doctor}"
