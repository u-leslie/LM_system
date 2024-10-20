from uuid import UUID
from django.shortcuts import redirect, render, get_object_or_404
from .models import Shipment
from .forms import ShipmentForm

def shipments_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipments/shipments_list.html', {'shipments': shipments})

# def shipment_detail(request, shipment_id):
#     shipment_id = UUID(shipment_id)
#     shipment = get_object_or_404(Shipment, shipment_id=shipment_id)
#     return render(request, 'shipments/shipment_detail.html', {'shipment': shipment})

def shipment_detail(request, shipment_id):
    # Convert the shipment_id to a UUID only if it's a string
    if isinstance(shipment_id, str):
        try:
            shipment_id = UUID(shipment_id)
        except ValueError:
            # Handle invalid UUID error
            return render(request, 'shipments/error.html', {'error': 'Invalid shipment ID'})
    
    # Fetch the shipment object using the shipment_id
    shipment = get_object_or_404(Shipment, shipment_id=shipment_id)
    
    # Render the shipment details in the template
    return render(request, 'shipments/shipment_detail.html', {'shipment': shipment})

def shipment_create(request):
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipments_list')
    else:
        form = ShipmentForm()
    return render(request, 'shipments/shipment_form.html', {'form': form})
