from rest_framework import serializers, viewsets, status as status_code, generics, mixins
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import permissions
import json

from .serializer import *
from .models import *

class TaskView(viewsets.ModelViewSet):
	serializer_class = TaskSerializer
	queryset = Task.objects.all().order_by('-id')
	filter_fields = ['title','user','date']
	http_method_names = ['get','post', 'put', 'patch']

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
