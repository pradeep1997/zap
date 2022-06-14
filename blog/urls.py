from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


app_name = 'blog'

urlpatterns = [
    path('', postlist, name='post-list'),
    path('post-detail/<str:slug>/', postDetail, name='post-detail'),
]
