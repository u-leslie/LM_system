from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link driver to a user
    name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
