from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "accounts/index.html")

def register(request):
    return HttpResponse("Register Page - Work in progress")

def login_view(request):
    return HttpResponse("Login Page - Work in progress")

def logout_view(request):
    return HttpResponse("Logout Page - Work in progress")

def profile(request):
    return HttpResponse("Profile Page - Work in progress")

def edit_profile(request):
    return HttpResponse("Edit Profile Page - Work in progress")


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
