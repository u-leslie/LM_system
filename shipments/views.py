from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shipment
from .forms import ShipmentForm

# List of all shipments (login required)
@login_required
def shipment_list(request):
    shipments = Shipment.objects.filter(user=request.user) 
    return render(request, 'shipments/shipments_list.html', {'shipments': shipments})

@login_required
def shipment_detail(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk, user=request.user)  
    return render(request, 'shipments/shipment_detail.html', {'shipment': shipment})

@login_required
def shipment_create(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False) 
            shipment.user = request.user  
            shipment.save()
            return redirect('shipments_list')
    else:
        form = ShipmentForm()

    return render(request, 'shipments/shipment_form.html', {'form': form})

@login_required
def shipment_edit(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk, user=request.user)  # Ensure the shipment belongs to the user
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipments_list')
    else:
        form = ShipmentForm(instance=shipment)
    
    return render(request, 'shipments/shipment_edit.html', {'form': form})

@login_required
def shipment_delete(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk, user=request.user)  # Ensure the shipment belongs to the user
    if request.method == 'POST':
        shipment.delete()
        return redirect('shipments_list')
    
    return render(request, 'shipments/shipment_delete.html', {'shipment': shipment})
