from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
]
