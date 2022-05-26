from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from datetime import datetime
from .models import *

class UserSerializer(serializers.ModelSerializer):
	token = serializers.SerializerMethodField()

	class Meta:
		model = User
		exclude = ('user_permissions','groups','password','is_staff','is_superuser','date_joined')
	
	def get_token(self, obj):
		token, created = Token.objects.get_or_create(user=obj)
		return token.key

class UserLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password',)
		extra_kwargs = {
			'username': {'required': True, 'validators': []},
			'password': {'required': True, 'style': {'input_type': 'password'}},
		}
	
	def to_representation(self, instance):
		serializer = UserSerializer(instance=instance)
		return serializer.data

	def create(self, validated_data):
		user = authenticate(username=validated_data['username'], password=validated_data['password'],)
		if user is not None:
			return user
		raise serializers.ValidationError({"detail":'Invalid username or password.'})

class UserCreationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'},write_only=True)
	cpassword = serializers.CharField(style={'input_type': 'password'},write_only=True)

	class Meta:
		model = User
		fields = ('city', 'username','password','cpassword','email','mobile','first_name','last_name',)
		extra_kwargs = {
			'mobile': {'required': True},
			'first_name': {'required': True},
			'last_name': {'required': True},
		}

	def validate(self, data):
		if data['password'] != data['cpassword']:
			raise serializers.ValidationError({"cpassword":['Passwords do not match']})
		return data

	def to_representation(self, instance):
		serializer = UserSerializer(instance=instance)
		return serializer.data

	def create(self, validated_data):
		user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], mobile=validated_data['mobile'], first_name = validated_data['first_name'], last_name = validated_data['last_name'])
		return user


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('title', 'user', 'desc', 'date', 'status')