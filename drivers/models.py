from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
