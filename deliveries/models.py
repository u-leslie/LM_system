from django.db import models
from shipments.models import Shipment
from drivers.models import Driver

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
]


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)  
    delivery_date = models.DateTimeField()  
    delivery_status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    delivered_by = models.CharField(max_length=100)  
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)  
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)  # Adjust as needed

    def __str__(self):
        return f'Delivery {self.delivery_id} - {self.delivery_status}'