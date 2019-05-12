from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Tip
from .forms import PostForm, UserCreateForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
# 以下のインポート文は新規会員登録で追加
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView

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

# アカウント作成
"""
class CreateAccount(CreateView):
	form_class = UserCreationForm
	template_name = 'blog/signup.html' 
	success_url = reverse_lazy('post_list')

	def form_valid(self, form):
		user = form.save() # formの情報を保存
		login(self.request, user) # 認証
		self.object = user
		return HttpResponseRedirect(self.get_success_url()) # リダイレクト
"""
def signup(request):
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect(to='../')
	else:
		form = UserCreateForm()
	return render(request, 'blog/signup.html', {'form': form})

def tip_list(request):
	tips = Tip.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request, 'blog/tip_list.html', {'tips': tips})