from django.shortcuts import get_object_or_404, render, redirect
from .models import Driver
from .forms import DriverForm  # assuming you have a DriverForm for handling the form

# List all drivers
def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/drivers_list.html', {'drivers': drivers})

# View details of a specific driver
def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})

# Create a new driver
def driver_create(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drivers_list')  # Redirect to the list view after saving
    else:
        form = DriverForm()

    return render(request, 'drivers/driver_create.html', {'form': form})

# Edit an existing driver
def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('drivers_list')
    else:
        form = DriverForm(instance=driver)
    
    return render(request, 'drivers/driver_edit.html', {'form': form})

# Delete a driver
def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('drivers_list')
    
    return render(request, 'drivers/driver_delete.html', {'driver': driver})
