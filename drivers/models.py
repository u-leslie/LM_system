from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
