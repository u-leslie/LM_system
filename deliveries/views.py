from django.shortcuts import get_object_or_404, render
from .models import Delivery

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'deliveries/delivery_list.html', {'deliveries': deliveries})

def delivery_detail(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    return render(request, 'deliveries/delivery_detail.html', {'delivery': delivery})
