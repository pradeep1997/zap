from rest_framework import serializers, viewsets, status as status_code, generics, mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from django.contrib.auth import authenticate
from rest_framework.response import Response
import json

from .serializer import *
from .models import *

class TaskView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated, )
	serializer_class = TaskSerializer
	queryset = Task.objects.all().order_by('-id')
	filter_fields = ['title','user','date']
	# http_method_names = ['get','post', 'put', 'patch', 'delete']

	def _allowed_methods(self):
		if self.request.user.role == 'Employee':
			return ['get', 'patch']
		if self.request.user.role == 'Client':
			return ['post']
		if self.request.user.role == 'Manager':
			return ['get','post', 'put', 'patch', 'delete']

class UserLoginView(viewsets.ModelViewSet):
	permission_classes = ((AllowAny,))
	queryset = User.objects.all().order_by('-id')
	serializer_class = UserLoginSerializer
	http_method_names = ['post']

class UserCreationView(viewsets.ModelViewSet):
	permission_classes = ((AllowAny,))
	queryset = User.objects.all().order_by('-id')
	serializer_class = UserCreationSerializer
	http_method_names = ['post']
