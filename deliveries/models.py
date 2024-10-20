from django.db import models
from shipments.models import Shipment

class Delivery(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    delivery_status = models.CharField(max_length=50, default="Pending")
    delivered_by = models.CharField(max_length=255)

    def __str__(self):
        return f"Delivery of {self.shipment.shipment_id} on {self.delivery_date}"
