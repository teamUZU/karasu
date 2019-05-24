from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Tip
from .forms import PostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator

def post_list(request, num=1):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	picks = Post.objects.filter(pickup_check=True).order_by('published_date').reverse()
	page = Paginator(posts, 11)
	return render(request, 'blog/post_list.html', {'posts': page.get_page(num), 'picks': picks})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	picks = Post.objects.filter(pickup_check=True).order_by('published_date').reverse()
	return render(request, 'blog/post_detail.html', {'post': post, 'picks': picks})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
	return render(request, 'blog/about.html')

def tip_list(request):
	tips = Tip.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request, 'blog/tip_list.html', {'tips': tips})

def tip_detail(request, pk):
	tip = get_object_or_404(Tip, pk=pk)
	return render(request, 'blog/tip_detail.html', {'tip': tip})