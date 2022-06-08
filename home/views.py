from django.shortcuts import render

from blog.models import *
# Create your views here.

def home(request):
	posts = Post.objects.filter(status='Active').all().order_by('-id')[:3]
	print(posts, 'ppppppppppppppppp')
	return render(request, 'home/index.html', {'posts':posts})