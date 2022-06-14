from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.staticfiles.storage import staticfiles_storage
from datetime import datetime, timedelta
from django.http import JsonResponse


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

def postDetail(request, slug):
	post = Post.objects.filter(slug=slug, status='Active').last()
	tags = Tag.objects.filter(status='Active').all()[:5]
	cats = Category.objects.filter(status='Active').all()[:5]
	ppost = Post.objects.filter(status='Active').exclude(id=post.id).all().order_by('-like')[:5]
	comments = Comment.objects.filter(reply__isnull=True, status='Active').all().order_by('-id')
	if request.method == 'POST':
		image = request.build_absolute_uri(staticfiles_storage.url('img/user.png'))
		type = request.POST.get('type', None)
		if type == 'comment-reply':
			c_id = request.POST.get('c_id', None)
			name = request.POST.get('name', None)
			email = request.POST.get('email', None)
			content = request.POST.get('content', None)
			if c_id and name and email and content:
				c_obj = Comment.objects.filter(id=int(c_id), post=post, status='Active').last()
				comment = Comment(post=post, name=name, email=email, content=content, reply=c_obj)
				comment.save()
				date_time = comment.timestamp + timedelta(hours=5, minutes=30)
				d = date_time.strftime("%B %d, %Y, %-H:%M%p")
				msg = '''
				<div class="d-flex">
				<div class="thumb">
						<img src="'''+str(image)+'''" class="user-story-image1">
				</div>
				<div>
				<h6><a href="#">'''+str(comment.name)+'''</a></h6>
				<small>'''+str(d)+'''</small>
				</div>
				</div>
				<p class="comment-content1">'''+str(comment.content)+'''</p>
				'''
				return JsonResponse({'msg':msg}, safe=False)
			if name and email and content:
				comment = Comment(post=post, name=name, email=email, content=content)
				comment.save()
				date_time = comment.timestamp + timedelta(hours=5, minutes=30)
				d = date_time.strftime("%B %d, %Y, %-H:%M%p")
				msg = '''
				<div class="d-flex">
				<div class="thumb">
						<img src="'''+str(image)+'''" class="user-story-image">
				</div>
				<div>
				<div>
				<h6><a href="#">'''+str(comment.name)+'''</a></h6>
				<small>'''+str(d)+'''</small>
				</div>
				</div>
				<button class="ml-auto btn-reply text-uppercase reply-btns btn btn-primary" data-id="'''+str(comment.id)+'''">Reply</button>
				</div>
				<p class="comment-content">'''+str(comment.content)+'''</p>
				<form class="reply-forms reply-form'''+str(comment.id)+''' mb-3">
					<input type="hidden" name="comment_id" value="'''+str(comment.id)+'''">
					<div class="row mb-3">
						<div class="col">
							<input type="text" name="name" class="form-control" placeholder="Full Name" aria-label="Full Name" required>
						</div>
						<div class="col">
							<input type="email" name="email" class="form-control" placeholder="Email Address" aria-label="Email" required>
						</div>
					</div>
					<div class="mb-3">
						<textarea class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Say something here..." required></textarea>
					</div>
					<button class="main-btn btn btn-primary" type="submit">Post comment</button>
				</form>
				<div class="replys replys'''+str(comment.id)+''' ml-5 pl-3"></div>
				'''
				return JsonResponse({'msg':msg}, safe=False)
		else:
			story_id = request.POST.get('story_id', None)
			if story_id:
				obj = Story.objects.filter(id=story_id, status='Active').last()
				if type == 'like':
					obj.like +=1
					obj.save()
					print(obj.like, 'ppppppppppppppp')
					return JsonResponse({'like':'like', 'count':obj.like})
				if type == 'dislike':
					obj.dislike +=1
					obj.save()
					return JsonResponse({'like':'dislike','count':obj.dislike})
	return render(request, 'blog/post_detail.html', {'post':post, 'tags':tags, 'cats':cats, 'pposts':ppost, 'comments':comments})