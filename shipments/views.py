from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Shipment
from .forms import ShipmentForm

# List of all shipments
def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipments/shipments_list.html', {'shipments': shipments})

# Shipment details
def shipment_detail(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    return render(request, 'shipments/shipment_detail.html', {'shipment': shipment})

def shipment_create(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()  # Django automatically assigns the primary key
            return redirect('shipments_list')
    else:
        form = ShipmentForm()
    return render(request, 'shipments/shipment_form.html', {'form': form})

# Edit a shipment
def shipment_edit(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipments_list')
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipments/shipment_edit.html', {'form': form})

# Delete a shipment
def shipment_delete(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    if request.method == 'POST':
        shipment.delete()
        return redirect('shipments_list')
    return render(request, 'shipments/shipment_delete.html', {'shipment': shipment})
