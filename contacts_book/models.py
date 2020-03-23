from django.db import models

class Contacts(models.Model):
	name = models.CharField(max_length=200)
	mail = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	postalcode = models.CharField(max_length=10)

	def __str__(self):
		return self.name