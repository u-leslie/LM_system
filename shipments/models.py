from django.db import models
from drivers.models import Driver
from customers.models import Customer

class Shipment(models.Model):
    tracking_number = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])
    created_at = models.DateTimeField(auto_now_add=True)
