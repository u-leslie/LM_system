from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shipments.models import Shipment 
from drivers.models import Driver

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home after registration
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Home View
def home(request):
    return render(request, 'home.html')

# User Profile View (Show user's shipments and drivers)
@login_required
def profile(request):
    shipments = Shipment.objects.filter(user=request.user)  # Only show the shipments created by the logged-in user
    drivers = Driver.objects.filter(user=request.user)  # Only show the drivers created by the logged-in user
    return render(request, 'accounts/profile.html', {'shipments': shipments, 'drivers': drivers})
