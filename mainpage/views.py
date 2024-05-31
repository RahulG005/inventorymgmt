from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from mainpage.forms import UserRegistrationForm

# Create your views here.
def main_page(request):
    return render(request,'mainpage/main_page.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a home page or dashboard after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm(auto_id = False)
        form.fields['username'].widget.attrs['autocomplete'] = 'off'
        form.fields['password'].widget.attrs['autocomplete'] = 'off'
        form.fields['username'].widget.attrs['placeholder'] = 'Username'
        form.fields['password'].widget.attrs['placeholder'] = 'Password'
    return render(request, 'mainpage/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.') 
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
        form.fields['username'].widget.attrs['placeholder'] = 'Username'
        form.fields['email'].widget.attrs['placeholder'] = 'Email'
        form.fields['password1'].widget.attrs['placeholder'] = 'Password'
        form.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    return render(request, 'mainpage/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout