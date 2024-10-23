from django import forms
from .models import Delivery

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['delivery_date', 'delivery_status', 'delivered_by', 'shipment', 'driver']
        widgets = {
            'delivery_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'delivery_status': forms.Select(),
            'delivered_by': forms.TextInput(attrs={'placeholder': 'Enter name of person delivering'}),
            'shipment': forms.Select(),
            'driver': forms.Select(),
        }
