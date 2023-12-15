from django.db import models

from datetime import date, time


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
        return f"{self.doctor} - {self.specialization}"


class Visit(models.Model):
    date = models.DateField()
    start_time = models.TimeField(default=time(8))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Visit doctor {self.doctor} at {self.start_time} on {self.date}."
