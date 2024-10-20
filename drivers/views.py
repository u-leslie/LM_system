from django.shortcuts import get_object_or_404, render
from .models import Driver

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})
