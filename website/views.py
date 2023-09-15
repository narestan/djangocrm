from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page


# Create your views here.
@csrf_protect
def home(request):
    
    # check to see if logging in 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username= username, password=password)
        if user  is not  None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was have a problem with your user name or password")
            return redirect('home')
        
    else:            
        return render(request, 'home.html', {})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register(request):
    return render(request, 'register.html', {})

