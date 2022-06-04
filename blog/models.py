from django.db import models

# Create your models here.
status = (("Active", "Active"), ("Inactive", "Inactive"), ("Delete", "Delete"))

class Category(models.Model):
	title = models.CharField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add = True)
	utimestamp = models.DateTimeField(auto_now = True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Active')

	