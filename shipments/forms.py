from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['origin', 'destination', 'status', 'driver']
        widgets = {
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Origin'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
        }
