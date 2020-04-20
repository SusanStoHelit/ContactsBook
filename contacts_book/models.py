from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Contacts(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z| ]*$', 'Only alphanumeric characters are allowed.')
	val_phone = RegexValidator(r'^[\+|0-9][0-9]*$','Only Number or international format e.g +3531234567')
	val_email = EmailValidator('Invalid Email address.')
	name = models.CharField(max_length=200, validators=[alphanumeric])
	mail = models.CharField(max_length=200, validators=[val_email])
	phone = models.CharField(max_length=15, validators=[val_phone])
	address = models.CharField(max_length=200, validators=[alphanumeric])
	city = models.CharField(max_length=100, validators=[alphanumeric])
	country = models.CharField(max_length=100, validators=[alphanumeric])
	postalcode = models.CharField(max_length=10, validators=[alphanumeric])
	userowner = models.CharField(max_length=100)

	def __str__(self):
		return self.name