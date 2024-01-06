from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm ,SetPasswordForm
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, 'Signup successful. Please login.')
            return redirect('login2')
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           user = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=user, password=password)
           if user is not None:
               login(request, user)
               messages.success(request, 'You have successfully logged in!')
               return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'login2.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('login2')
    

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'password_change.html', {'form': form , 'title': 'Change Password'})

def password_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = SetPasswordForm(request.user)

    return render(request, 'password_change.html', {'form': form, 'title': 'Change without old Password'})