from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import api, views

router = DefaultRouter()
router.register('signup', api.UserCreationView, basename='sign_api')
router.register('login', api.UserLoginView, basename='login_api')
router.register('task', api.TaskView, basename='task')

urlpatterns = []