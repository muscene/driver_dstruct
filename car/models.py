from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional owner-related information can be added here


class Car(models.Model):
    # Car information
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class GeolocationData(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    speed = models.FloatField()


class StabilityData(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    stability_metric = models.FloatField()


class DriverBehaviorData(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    alcohol_level = models.FloatField()
    drowsiness_detected = models.BooleanField(default=False)
    distraction_detected = models.BooleanField(default=False)


class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car, blank=True)

    # Additional driver-related information can be added here
