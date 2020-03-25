from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contacts
		fields = ["name", "mail", "phone", "address", "city", "country", "postalcode"]