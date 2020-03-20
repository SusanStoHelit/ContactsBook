from django.shortcuts import render,redirect

def home(request):
	return render(request, 'home.html',{})

def add_contact(request):
	return render(request, 'add_contact.html',{})
