from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    # Implement login logic
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')
