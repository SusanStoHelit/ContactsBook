from django.shortcuts import render,redirect
from .models import Contacts
from .forms import ContactForm
from django.contrib import messages

def home(request):
	all_contacts = Contacts.objects.all
	return render(request, 'home.html',{'all_contacts':all_contacts})

def add_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			form.save()
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