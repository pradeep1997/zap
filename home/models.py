from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

gender = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
status = (("Active", "Active"), ("Inactive", "Inactive"), ("Delete", "Delete"))

class User(AbstractUser):
	email = models.EmailField(blank=False)
	mobile = models.CharField(max_length=15)
	gender = models.CharField(max_length=6, choices=gender, default='Male')
	dob = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='user/', blank=True, null=True)
	about = models.TextField(blank=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	address1 = models.CharField(max_length=100, null=True, blank=True)
	address2 = models.CharField(max_length=100, null=True, blank=True)
	postcode = models.CharField(max_length=10, blank=True, null=True)
	website = models.URLField(max_length=100, blank=True)
	timestamp = models.DateTimeField(auto_now_add = True)
	utimestamp = models.DateTimeField(auto_now = True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "01. Users"
	
	@property
	def full_name(self):
		if self.first_name and self.last_name:
			return str(self.first_name)+' '+str(self.last_name)
		return self.username

	def __str__(self):
		return str(self.username)

class Team(models.Model):
	degignations = (
		('backend developer', 'backend developer'), 
		('frontend developer', 'frontend developer'),
		('executive', 'executive'),
		('technical support', 'technical support'),
		('ceo', 'ceo'),
		('cto', 'cto'),
		('designer', 'designer')
		)
	name = models.CharField(max_length=160)
	designation = models.CharField(max_length=20, choices=degignations, default='backend developer')
	facebook = models.URLField(max_length=160, null=True, blank=True)
	twitter = models.URLField(max_length=160, null=True, blank=True)
	instagram = models.URLField(max_length=160, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add = True)
	utimestamp = models.DateTimeField(auto_now = True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Active')

	class Meta:
		verbose_name_plural = "02. Teams"

	def __str__(self):
		return str(self.name)