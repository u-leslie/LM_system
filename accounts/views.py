from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from deliveries.models import Delivery
from shipments.models import Shipment 
from drivers.models import Driver

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                request.session['username'] = user.username 
                request.session['last_login'] = str(datetime.now())  
                request.session.set_expiry(3600) 

                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# def home(request):
#     return render(request, 'home.html')

@login_required
def profile(request):
    shipments = Shipment.objects.filter(user=request.user) 
    drivers = Driver.objects.filter(user=request.user) 
    return render(request, 'accounts/profile.html', {'shipments': shipments, 'drivers': drivers})


def home(request):
    shipment_count = Shipment.objects.count()
    delivery_count = Delivery.objects.count()
    driver_count = Driver.objects.count()
    pending_tasks_count = Delivery.objects.filter(delivery_status='Pending').count()  # Adjust as needed

    context = {
        'shipment_count': shipment_count,
        'delivery_count': delivery_count,
        'driver_count': driver_count,
        'pending_tasks_count': pending_tasks_count,
    }
    return render(request, 'home.html', context)