from django.shortcuts import render,redirect
from .models import Contacts
from .forms import ContactForm, SignUpForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
import logging
logger = logging.getLogger('django.server')

def home(request):
	all_contacts = Contacts.objects.filter(userowner=request.user.username)
	return render(request, 'home.html',{'all_contacts':all_contacts})

def login_user(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        messages.success(request,('You have been loggen in!'))
	        logger.info('Someone logged in')
	        return redirect('home')
	    else:
	    	messages.success(request,('Error Logging in - Please try again...'))
	    	logger.error('Error, failed login')
	    	return redirect('login')
	else:
		return render(request, 'login.html')
def logout_user(request):
	logout(request)
	messages.success(request,('You have been logged out...'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data['username']
			password= form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request,user)
			messages.success(request,('You have registered!'))
			return redirect('home')
	else:
		form = SignUpForm()
	context = {'form': form}
	return render(request,'register.html', context)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()			
			messages.success(request,('You have edited your account!'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)
	context = {'form': form}
	return render(request,'edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()			
			messages.success(request,('You have eddited your passowrd!'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)
	context = {'form': form}
	return render(request,'change_password.html', context)



def add_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			instance = form.save()
			instance.userowner = request.user.username
			instance.save()
			messages.success(request, ('Contact has been added!!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems like there was an error......!'))
			return render(request,'add_contact.html',{})
	else:
		return render(request, 'add_contact.html',{})

def edit(request, list_id):
	if request.method == 'POST':
		current_contact = Contacts.objects.get(pk=list_id)
		form = ContactForm(request.POST or None, instance=current_contact)
		if form.is_valid():
			form.save()
			messages.success(request, ('Contact has been edited!!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems like there was an error......!'))
			return render(request,'edit.html',{})
	else:
		get_contact = Contacts.objects.get(pk=list_id)
		return render(request, 'edit.html',{'get_contact':get_contact})

def delete(request, list_id):
	if request.method == 'POST':
		current_contact = Contacts.objects.get(pk=list_id)
		current_contact.delete()
		messages.success(request, ('Contact has been deleted!!'))
		return redirect('home')		
	else:
		messages.success(request, ('Nothing has been deleted!!'))
		return redirect('home')	