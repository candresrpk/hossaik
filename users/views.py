from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


def signupView(request):
    form = UserCreationForm
    
    context = {
        'form': form,
    }
    
    if request.method == 'GET':
        return render(request, 'users/signup.html', context)
    
    if request.POST['password1'] == request.POST['password2']:
        
        try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        
        except ImportError as e:
            context['error'] = 'An error occurred: User already exists'
            return render(request, 'users/signup.html', context)
        
        except Exception as e:
            context['error'] = str(e)
            return render(request, 'users/signup.html', context)
        
    else:
        context['error'] = str('Passwords do not match')
        return render(request, 'users/signup.html', context)
    
    
def signinView(request):
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    
    if request.method == 'GET':
        return render(request, 'users/signin.html', context)
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        context['error'] = 'Invalid username or password'
        return render(request, 'users/signin.html', context)
    
    
def signoutView(request):
    logout(request)
    return redirect('home')