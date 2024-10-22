# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse
# from .models import Shipment
# from .forms import ShipmentForm

# # List of all shipments
# def shipment_list(request):
#     shipments = Shipment.objects.all()
#     return render(request, 'shipments/shipments_list.html', {'shipments': shipments})

# # Shipment details
# def shipment_detail(request, pk):
#     shipment = get_object_or_404(Shipment, pk=pk)
#     return render(request, 'shipments/shipment_detail.html', {'shipment': shipment})

# def shipment_create(request):
#     if request.method == 'POST':
#         form = ShipmentForm(request.POST)
#         if form.is_valid():
#             form.save()  # Django automatically assigns the primary key
#             return redirect('shipments_list')
#     else:
#         form = ShipmentForm()
#     return render(request, 'shipments/shipment_form.html', {'form': form})

# # Edit a shipment
# def shipment_edit(request, pk):
#     shipment = get_object_or_404(Shipment, pk=pk)
#     if request.method == 'POST':
#         form = ShipmentForm(request.POST, instance=shipment)
#         if form.is_valid():
#             form.save()
#             return redirect('shipments_list')
#     else:
#         form = ShipmentForm(instance=shipment)
#     return render(request, 'shipments/shipment_edit.html', {'form': form})

# # Delete a shipment
# def shipment_delete(request, pk):
#     shipment = get_object_or_404(Shipment, pk=pk)
#     if request.method == 'POST':
#         shipment.delete()
#         return redirect('shipments_list')
#     return render(request, 'shipments/shipment_delete.html', {'shipment': shipment})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shipment
from .forms import ShipmentForm

# List of all shipments (login required)
@login_required
def shipment_list(request):
    shipments = Shipment.objects.filter(user=request.user)  # Show only the shipments created by the logged-in user
    return render(request, 'shipments/shipments_list.html', {'shipments': shipments})

# Shipment details (login required)
@login_required
def shipment_detail(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk, user=request.user)  # Ensure the shipment belongs to the user
    return render(request, 'shipments/shipment_detail.html', {'shipment': shipment})

# Create a new shipment (login required)
@login_required
def shipment_create(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)  # Get the form data without saving it to the DB yet
            shipment.user = request.user  # Assign the logged-in user as the owner
            shipment.save()
            return redirect('shipments_list')
    else:
        form = ShipmentForm()

    return render(request, 'shipments/shipment_form.html', {'form': form})

# Edit an existing shipment (login required)
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

# Delete a shipment (login required)
@login_required
def shipment_delete(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk, user=request.user)  # Ensure the shipment belongs to the user
    if request.method == 'POST':
        shipment.delete()
        return redirect('shipments_list')
    
    return render(request, 'shipments/shipment_delete.html', {'shipment': shipment})
