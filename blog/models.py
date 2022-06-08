from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django_extensions.db.fields import AutoSlugField

from home.models import *
# Create your models here.
status = (("Active", "Active"), ("Inactive", "Inactive"), ("Delete", "Delete"))

class Category(models.Model):
	title = models.CharField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add = True)
	utimestamp = models.DateTimeField(auto_now = True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Active')

	def __str__(self):
		return str(self.title)

class Tag(models.Model):
	title = models.CharField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add = True)
	utimestamp = models.DateTimeField(auto_now = True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Active')

	def __str__(self):
		return str(self.title)

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='post_user')
	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_post')
	tags = models.ManyToManyField(Tag)
	title = models.CharField(max_length=160)
	slug = AutoSlugField(populate_from='title', max_length=160, editable=False, unique=True)
	desc = models.TextField(help_text='short description')
	content = RichTextUploadingField(help_text = "Content")
	image = models.ImageField(upload_to='post/images/')
	like = models.PositiveIntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add = True)
	utimestamp = models.DateTimeField(auto_now = True)
	track = models.TextField(blank=True, editable=False)
	utrack = models.TextField(blank=True, editable=False)
	status = models.CharField(max_length=10, choices=status, default='Active')

	def __str__(self):
		return str(self.title)



	