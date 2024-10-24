from django.shortcuts import redirect, render

from deliveries.forms import DeliveryForm
from .models import Delivery

def deliveries_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'deliveries/deliveries_list.html', {'deliveries': deliveries})

def delivery_detail(request, delivery_id):
    delivery = Delivery.objects.get(delivery_id=delivery_id)
    return render(request, 'deliveries/delivery_detail.html', {'delivery': delivery})


def delivery_create(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deliveries_list')  # Redirect to a delivery list or success page
    else:
        form = DeliveryForm()
    
    return render(request, 'deliveries/delivery_create.html', {'form': form})