from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from usersapp.forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register(request):
	if request.method == 'POST' :
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request,user)	
			messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')					
			return redirect('home')
	else :
		form = UserRegistrationForm()
	return render(request,'registration/register.html',{'form' : form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie.")
                next = request.GET.get('next', '/')
                return redirect(next)
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')
