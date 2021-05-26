from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)
from .forms import (
	UserLoginForm, 
	UserRegisterForm,
	NewsPostForm,
	PostCommentForm
)
from .models import News, Comment


def error_404(request, exception):
	context ={
		}
	return render(request, 'SocialApp/404.html', context)


def index_view(request):
	context = {
		'request':request
	}
	return render(request, 'SocialApp/Index.html',context)


def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username = username, password = password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		'form':form,
	}
	return render(request, 'SocialApp/Log_In.html', context)


def signup_view(request):
	next = request.GET.get('next')
	form = UserRegisterForm(request.POST or None)

	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		'form':form,
	}
	return render(request, 'SocialApp/Sign_Up.html', context)


@login_required
def create_news_view(request):
	form = NewsPostForm(request.POST or None)
	
	if form.is_valid():
		news = form.save(commit = False)
		news.user = request.user
		news.save()
		return redirect('social_news')

	context = {
		'form':form,
	}
	return render(request, 'SocialApp/Create_News.html', context)


@login_required
def news_view(request):
	news = News.objects.all()	
	
	page_number = request.GET.get('page')
	
	if not page_number:
		page_number = 1

	page_number = int(page_number)
	page_capacity = 3

	if len(news) % page_capacity != 0:
		page_count = len(news) // page_capacity + 1
	else:
		page_count = len(news) // page_capacity

	news_start = page_capacity * (page_number - 1) 
	news_end = news_start + page_capacity


	news = news[news_start:news_end]

	context = {
		'news':news,
		'page_count':range(1, page_count + 1)
	}
	return render(request, 'SocialApp/News.html', context)

@login_required
def post_view(request, id):
	post = News.objects.get(id=id)
	comments = Comment.objects.filter(news__id = id)
	form = PostCommentForm(request.POST or None)

	if form.is_valid():
		comment = form.save(commit = False)
		comment.news = post
		comment.user = request.user
		comment.save()
		return redirect('social_post',id)

	context = {
		'form':form,
		'post':post,
		'comments':comments,
		}
	return render(request, "SocialApp/Post.html", context)



def logout_view(request):
	logout(request)
	return redirect('/')