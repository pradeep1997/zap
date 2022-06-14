from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
# Create your views here.

def postlist(request):
	posts = Post.objects.filter(status='Active').all()
	page = request.GET.get('page', 1)

	paginator = Paginator(posts, 6)
	try:
		page_obj = paginator.page(page)
	except PageNotAnInteger:
		page_obj = paginator.page(1)
	except EmptyPage:
		page_obj = paginator.page(paginator.num_pages)
	return render(request, 'blog/post_list.html', {'page_obj': page_obj})